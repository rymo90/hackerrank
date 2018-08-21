m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))
res = M.difference(N)
r = N.difference(M)
lista = sorted(list(res.union(r)))
for _ in lista:
    print(_)
