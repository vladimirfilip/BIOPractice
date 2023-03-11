from math import factorial


def nCr(n, r):
    f = factorial
    return f(n) // f(r) // f(n - r)


n = int(input())
movies = list(range(1, n + 1))
values = {i: [] for i in movies}
for _ in range(nCr(n, 2)):
    s = input()
    m1, m2 = tuple(list(map(int, s.split())))
    values[m1].append(m2)
movie_order = sorted(movies, reverse=True, key=lambda x: len(values[x]))


def perms(l: list):
    if len(l) == 1:
        yield l
        return
    for i in range(len(l)):
        rest = l[:i] + l[i + 1:]
        for perm in perms(rest):
            if l[i] in values[perm[0]]:
                result = [l[i]] + perm
                yield result


print(" ".join(list(map(str, next(perms(movie_order))))))
