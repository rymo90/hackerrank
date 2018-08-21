from collections import Counter
shoes = int(input())
shoesSize = map(int, input().split())
shoesSize = Counter(shoesSize)
custmers = int(input())
totalEarned = 0
for _ in range(custmers):
    size, Price = map(int, input().split())
    if shoesSize[size]:
        shoesSize[size] -= 1
        totalEarned += Price

print(totalEarned)
