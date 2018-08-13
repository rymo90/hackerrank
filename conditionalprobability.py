n = int(input())
sets = ""
b = ""
prop = ""
for _ in range(n):
    sets = input().split()
    b = input().split()
    prop = input().split()
print(sets, b, prop)

pB = len(b)/len(sets)
print("pB", pB)
pA = len(prop)/(len(sets)*3)
pAB = pA*pB/pB
print(pAB == 1/3)
