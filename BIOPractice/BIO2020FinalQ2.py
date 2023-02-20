c = int(input())


def get_dist(*args):
    x1, y1, x2, y2 = tuple(args)
    delta_x, delta_y = abs(x1 - x2), abs(y1 - y2)
    return delta_x + delta_y - min(delta_x, delta_y)

#for i in range(c):

x1, y1, x2, y2 = tuple(map(int, input().split()))
print(get_dist(x1, y1, x2, y2))
