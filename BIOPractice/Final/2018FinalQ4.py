from math import sqrt, atan2, pi

s, l = tuple(map(int, input().split()))
points = []
min_x, max_x = float('inf'), 0
min_y, max_y = float('inf'), 0


def get_dist(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return sqrt(dx * dx + dy * dy)


def get_angle(x1, y1, x2, y2):
    #
    # Gets angle of point (x2, y2) from point (x1, y1)
    #
    dy = y2 - y1
    dx = x2 - x1
    theta = atan2(dy, dx) * 180 / pi
    if theta < 0:
        theta += 360
    return theta


for _ in range(s * l):
    x, y = tuple(map(int, input().split()))
    points.append((_ + 1, x, y))

cx = (min(p[1] for p in points) + max(p[1] for p in points)) / 2
cy = (min(p[2] for p in points) + max(p[2] for p in points)) / 2

sorted_points = sorted(points, key=lambda p: get_dist(cx, cy, p[1], p[2]), reverse=True)
for i in range(0, len(sorted_points), s):
    loop = sorted_points[i:i + s]
    loop.sort(key=lambda p: get_angle(cx, cy, p[1], p[2]))
    print(" ".join(str(p[0]) for p in loop))
