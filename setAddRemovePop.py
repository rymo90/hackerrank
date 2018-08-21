int(input())
sets = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    comand = input().split()
    if comand[0] == "pop":
        sets.pop()
    elif comand[0] == "remove":
        sets.remove(int(comand[1]))
    else:
        sets.discard(int(comand[1]))

print(sum(sets))
