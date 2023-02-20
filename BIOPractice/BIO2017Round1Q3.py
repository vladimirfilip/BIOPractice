from functools import lru_cache
import sys

p, i, n, w = tuple(list(map(int, sys.argv[1:])))


def perms_of_parcel_distribution(total: int, num_parcels: int):
    if num_parcels == 1:
        yield [total]
        return
    for i in range(1, total + 2 - num_parcels):
        for perm in perms_of_parcel_distribution(total - i, num_parcels - 1):
            yield [i] + perm


@lru_cache(maxsize=None)
def parcel_perms(w: int, length: int, max_val: int):
    if w == 0:
        return [[]]
    if w == 1:
        return [[1]]
    result = []
    for i in range(1, min(w + 1, max_val + 1)):
        for perm in parcel_perms(w - i, length - 1, max_val):
            new_perm = sorted([i] + perm)
            if len(new_perm) != length or new_perm in result:
                continue
            result.append(new_perm)
    return result


result = 0
for perm in perms_of_parcel_distribution(n, p):
    found = False
    current = 0
    for length in perm:
        possible_parcels = parcel_perms(w, length, i)
        if possible_parcels == [[]]:
            continue
        if not found:
            found = True
            current = 1
        current *= len(possible_parcels)
    result += current
print(result)
