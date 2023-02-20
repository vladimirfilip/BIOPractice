import sys
from functools import lru_cache
from queue import SimpleQueue


p, q, r = tuple(map(int, input().split()))
i = int(input())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = alphabet[:p]


class Node:
    def __init__(self, parent, depth: int, letter: str, chain_length: int):
        self.parent = parent
        self.depth = depth
        self.num_children = 0
        self.letter = letter
        self.children = []
        if depth < r:
            self.create_children(chain_length)
            self.num_children = sum([child.num_children for child in self.children])
        else:
            self.num_children = 1

    def create_children(self, chain_length: int):
        for letter in letters:
            if self.letter and letter == self.letter[-1] and chain_length == q:
                continue
            new_child = Node(self, self.depth + 1, self.letter + letter, chain_length + 1 if self.letter and letter == self.letter[-1] else 1)
            self.children.append(new_child)


root = Node(None, 0, "", 0)
n = i
nodes = [[] for _ in range(r + 1)]
queue = SimpleQueue()
queue.put(root)
while not queue.empty():
    node = queue.get()
    nodes[node.depth].append(node.num_children)
    for child in node.children:
        queue.put(child)
for row in nodes:
    print(" ".join(str(node) for node in row))
#print(root.letter)

#
# @lru_cache(maxsize=None)
# def count(prefix: str, required_length: int):
#     global n
#     chain_length = len(prefix) - len(prefix.rstrip(prefix[-1])) if prefix else 0
#     if chain_length > q:
#         return 0
#     if len(prefix) == required_length:
#         n += 1
#         if n == i:
#             print(prefix)
#             exit(0)
#         return 1
#     result = 0
#     for letter in letters:
#         new_prefix = prefix + letter
#         if prefix and letter != prefix[-1]:
#             result += count(letter, required_length - len(new_prefix))
#
#         result += count(new_prefix, required_length)
#     return result

#print(result)
