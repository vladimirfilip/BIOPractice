from queue import SimpleQueue


class Path:
    def __init__(self, t: int, val: int, i: int):
        self.satisfaction = val
        self.telescopes_visited = t
        self.pos = i


t, w = tuple(map(int, input().split()))
telescope_values = []
result = 0


def calculate_max_satisfaction(t_max: int) -> int:
    i = 0
    start_path = Path(1, telescope_values[i], i)
    q = SimpleQueue()
    q.put(start_path)
    max_satisfaction = 0
    while not q.empty():
        path = q.get()
        t, val, i = path.telescopes_visited, path.satisfaction, path.pos
        if val > max_satisfaction:
            max_satisfaction = val
        if t == t_max:
            continue
        if i > 0:
            q.put(Path(t + 1, val + telescope_values[i - 1], i - 1))
        if i < len(telescope_values) - 1:
            q.put(Path(t + 1, val + telescope_values[i + 1], i + 1))
    return max_satisfaction


for _ in range(t):
    telescope_values.append(int(input()))
for _ in range(w):
    result += calculate_max_satisfaction(int(input()))
print(result)
