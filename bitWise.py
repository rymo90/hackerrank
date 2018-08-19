t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    maxValue = 0

    for i in range(1, n+1):
        j = i+1
        for j in range(i+1, n+1):
            temp = int(bin(i & j), 2)
            if temp < k:
                if temp > maxValue:
                    maxValue = temp

    print(maxValue)
