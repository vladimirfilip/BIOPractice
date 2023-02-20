from functools import lru_cache

s, i = tuple(input().split())
i = int(i)


@lru_cache(maxsize=None)
def get_possible_positions(index: int, cumulative_spaces: str) -> list[int]:
    result = []
    for i in range(index, -1, -1):
        if i == index:
            result.append(index)
            continue
        if cumulative_spaces[i] == "0":
            break
        result.append(i)
    return result[::-1]


def normalise(s: str) -> str:
    return "".join("1" if char.isalpha() else "0" for char in s)


alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = alphabet[:len(s)]

d = []
for j in range(len(letters) - 1, -1, -1):
    new_car = letters[j]
    placement_of_new_car = s.index(new_car)
    prev_arrangement = s.replace(new_car, " ")
    d.append(get_possible_positions(placement_of_new_car, normalise(prev_arrangement)))
    s = prev_arrangement
d = d[::-1]


def index_to_place(index: int) -> str:
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[index]


def succeeding_combos(l: list[list[int]], i: int) -> int:
    n = None
    for p in range(i + 1, len(l)):
        if not n:
            n = 1
        n *= len(l[p])
    return n if n is not None else 1


result = []
i -= 1
for j in range(len(d)):

    indexes = d[j]
    quotient = succeeding_combos(d, j)
    k = i // quotient
    result.append(indexes[k])
    i -= k * quotient

print("".join(index_to_place(i) for i in result))
