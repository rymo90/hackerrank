y = int(input())
x = [int(i) for i in input().split()]
x = list(set(x))

print(sum(x)/len(x))
