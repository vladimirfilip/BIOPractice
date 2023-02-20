from functools import lru_cache
from time import time


alphabet = "abcdefghijklmnopqrstuvwxyz"
result = 0


class Blockchain:
    def __init__(self, value, length):
        self.val = value
        self.max_length = length
        self.available_letters = self.calc_next_letter()
        if len(self.val) == self.max_length:
            global result
            result += 1
        else:
            for letter in self.available_letters:
                Blockchain(self.val + letter, length)

    @lru_cache(maxsize=None)
    def calc_letter_value(self, char: str) -> int:
        return alphabet.index(char)

    def calc_next_letter(self, latest_val=None) -> list[str]:
        #
        # Returns list of potential characters to be appended
        #
        cutoff_index = self.max_length
        for i in range(len(self.val) - 1):
            for j in range(i + 1, len(self.val)):
                first_val = self.calc_letter_value(self.val[i])
                second_val = self.calc_letter_value(self.val[j])
                if second_val > first_val:
                    cutoff_index = min(second_val, cutoff_index)
        result = [char for char in list(alphabet[:cutoff_index]) if char not in self.val]
        return result


l, p = input().split()

start_time = time()
Blockchain(p.lower(), int(l))
print(result)
print(time() - start_time)