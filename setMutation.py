input()
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    x = input()
    temp = x[0]
    if temp == "i":
        i = set(map(int, input().split()))
        a.intersection_update(i)
    elif temp == "u":
        u = set(map(int, input().split()))
        a.update(u)
    elif temp == "s":
        s = set(map(int, input().split()))
        a.symmetric_difference_update(s)
    else:
        d = set(map(int, input().split()))
        a.difference_update(d)

print(sum(a))
