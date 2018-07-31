
def mode(values: list) -> int:
    counters = dict()
    result = None
    for value in values:
        if value in counters:
            counters[value] += 1
        else:
            counters[value] = 1
        if (result is None) or counters[value] > counters[result]:
            result = value
        elif counters[value] == counters[result] and value < result:
            result = value
    return result


n = int(input())
kk = [int(i) for i in input().split()]
x = sorted(kk)
mean = 0
median = 0
for i in range(len(x)):
    mean += x[i]
fst = len(x)//2
if len(x) % 2 == 0:
    median = x[fst] + x[fst-1]
else:
    median = x[fst]


print(mean/n)
print(median/2)
print(mode(kk))
