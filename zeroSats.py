n = int(input())
x = [int(i) for i in input().split()]
w = [int(j) for j in input().split()]
result = 0
nem = 0
for _ in range(n):
    result += x[_]*w[_]
    nem += w[_]
print(round(result/nem, 1))
