n = int(input()) - 1

if n == 0:
    print(5)
    exit(0)


def get_number_combos(x: int):
    return 9 ** ((x - 1) // 2) if x % 2 == 1 else 9 ** (x // 2)


def to_base_9(n: int) -> str:
    base = 9
    new_num = ''
    while n > 0:
        new_num = str(n % base) + new_num
        n //= base
    return new_num


length = 0
cumulative_combos = 0
while cumulative_combos <= n:
    length += 1
    combos = get_number_combos(length)
    cumulative_combos += combos

cumulative_combos -= get_number_combos(length)
cumulative_combos = n - cumulative_combos
left_digit_length = (length - 1) // 2 if length % 2 else length // 2
left_digits = to_base_9(cumulative_combos).zfill(left_digit_length)
left_digits = [int(digit) + 1 for digit in left_digits]
right_digits = [10 - digit for digit in left_digits][::-1]
if length % 2 == 1:
    result = left_digits + [5] + right_digits
else:
    result = left_digits + right_digits
print("".join(list(map(str, result))))
