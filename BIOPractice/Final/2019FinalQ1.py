pigeons = list(range(1, int(input()) + 1)) # generates list of pigeons based on first line of input
# Program then takes next lines of input and applies movement offsets to each pigeon,
# storing movement deltas in a dictionary as the amount of places moved to the right
deltas = {i: 0 for i in pigeons}
while (s := input()) != "-1 -1":
    t = tuple(map(int, s.split()))
    deltas[min(t)] += 1
    deltas[max(t)] -= 1
# Applies movement offsets to create new arrangement
new_pigeons = [0 for _ in pigeons]
for i in pigeons:
    new_index = i - 1 + deltas[i]
    new_pigeons[new_index] = i
print(" ".join(list(map(str, new_pigeons))))
