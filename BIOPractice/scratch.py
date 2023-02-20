from math import pi, sqrt
from numpy import arccos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)


class Edge:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.length = self.get_length()

    def get_length(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return sqrt(dx * dx + dy * dy)


def get_angle(a: Edge, b: Edge, c: Edge):
    return arccos((c.length * c.length - a.length * a.length - b.length * b.length) / (-2 * a.length * b.length))


def get_edge(edges: dict, p1: Point, p2: Point):
    return list(set(edges[p1]).intersection(set(edges[p2]))).pop()


def get_k_from_n(l: list, k: int):
    if k == 0:
        yield ()
        return
    for i in range(len(l)):
        rest = l[i + 1:]
        for perm in get_k_from_n(rest, k - 1):
            yield tuple([l[i]]) + perm


s = ""
points = []
while s := input():
    x_coord, y_coord = tuple(map(float, s.split()))
    points.append(Point(x_coord, y_coord))

#
# Forms edges from each point to every other point
#
edges = {p: [] for p in points}
for p1 in edges:
    for p2 in edges:
        if p2 == p1:
            continue
        edge = Edge(p1, p2)
        edges[p1].append(edge)
        edges[p2].append(edge)
#
# Computes the internal angle at each point 'point' by forming triangle and stores the two points immediately
# adjacent to each point
#
interior_angles = {p: 0.0 for p in points}
adjacent_points = {p: () for p in points}
for point in points:
    for p1 in points:
        if p1 == point:
            continue
        for p2 in points:
            if p2 == point or p2 == p1:
                continue
            a = get_edge(edges, point, p1)
            b = get_edge(edges, point, p2)
            c = get_edge(edges, p1, p2)
            theta = get_angle(a, b, c)
            if theta > interior_angles[point]:
                adjacent_points[point] = (p1, p2)
                interior_angles[point] = theta
#
# Converts interior angles from radians to degrees
#
interior_angles = {k: v * 180 / pi for k, v in interior_angles.items()}
is_convex = True
for k, v in interior_angles.items():
    if v > 180:
        is_convex = False
    print(f"{k}: {v}")

if not is_convex:
    print("The shape described is not convex")
    exit(0)
print("The shape described is convex")


def get_area():
    #
    # Gets a point from the shape, and its two adjacent points, finds the area of the triangle and continues recursively
    # removing a triangle from the shape until there are none left
    #
    global points
    if len(points) < 3:
        return 0
    root = points.pop()
    point2, p3 = adjacent_points[root]
    edge1, edge2, hyp = get_edge(edges, root, point2), get_edge(edges, root, p3), get_edge(edges, point2, p3)
    angle = get_angle(edge1, edge2, hyp)
    return 0.5 * edge1.length * edge2.length * sin(angle) + get_area()


print("The area is", get_area())
