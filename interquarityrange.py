import math


def evenElement(lis):
    half = len(lis)//2
    return (lis[half-1]+lis[half])//2


def oddElement(lis):
    half = len(lis)//2
    return lis[half]


def qualities(x):
    result = []
    middle = 0
    lowerHalf = 0
    upperHalf = 0
    element = len(x)//2
    if len(x) % 2 == 0:
        middle = (x[element-1] + x[element])//2
        if len(x[:element]) % 2 == 0:
            lowerHalf = evenElement(x[:element])
            upperHalf = evenElement(x[element:])
        else:
            lowerHalf = oddElement(x[:element])
            upperHalf = oddElement(x[element:])
    else:
        middle = x[element]
        if len(x[:element]) % 2 == 0:
            lowerHalf = evenElement(x[:element])
            upperHalf = evenElement(x[element+1:])
        else:
            lowerHalf = oddElement(x[:element])
            upperHalf = oddElement(x[element:])

    result.extend((lowerHalf, upperHalf))
    return result


n = int(input())
x = [i for i in input().split()]
f = [int(j) for j in input().split()]
lis = []
for l in range(n):
    lis.extend([x[l]]*f[l])
lis.sort(key=int)
newlis = list(map(int, lis))
svar = qualities(newlis)
temp = svar[1]-svar[0]
ln = math.floor(temp*10)/10
print(ln)
