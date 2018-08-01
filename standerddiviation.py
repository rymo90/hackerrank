import math
n = int(input())
x = [int(i) for i in input().split()]
tel = 0
for _ in range(len(x)):
    tel += x[_]
q = tel/n
div = 0
for i in range(n):
    div += math.pow(x[i]-q, 2)
print(round(math.sqrt(div/n), 1))
