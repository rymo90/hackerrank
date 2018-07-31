def evenElement(lis):
    half = len(lis)//2
    return (lis[half-1]+lis[half])//2


def oddElement(lis):
    half = len(lis)//2
    return lis[half]


def qualities(lis):
    result = []
    middle = 0
    lowerHalf = 0
    upperHalf = 0
    element = len(x)//2
    if len(lis) % 2 == 0:
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

    result.extend((lowerHalf, middle, upperHalf))
    return result


n = int(input())
x = [int(i) for i in input().split()]
x = sorted(x)
svar = qualities(x)
for _ in svar:
    print(_)
