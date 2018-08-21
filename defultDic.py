from collections import defaultdict
a, b = map(int, input().split())
lis = defaultdict(list)

for i in range(a):
    temp = input()
    lis[temp].append(i+1)

for _ in range(b):
    key = input()
    if len(lis[key]) > 0:
        print(" ".join(str(c) for c in lis[key]))
    else:
        print(-1)
