from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(*list(product(a, b)))
