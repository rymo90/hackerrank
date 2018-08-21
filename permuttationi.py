from itertools import permutations
import textwrap
s = input().split()
permutation = list(permutations(s[0], int(s[1])))
for i in sorted(permutation):
    print("".join(i))
