from collections import namedtuple
n = int(input())
k = input()
info = namedtuple("Score", k)
result = 0
for i in range(n):
    temp = input().split()
    data = info(temp[0], temp[1],
                temp[2], temp[3])

    result += int(data.MARKS)

print(result/n)
