from collections import OrderedDict, defaultdict
n = int(input())
orderItem = OrderedDict()
lista = []
for _ in range(n):
    item = input().split()
    names = " ".join(item[:-1])
    price = int("".join(item[-1:]))
    if names in lista:
        orderItem[names] += price
    else:
        lista.append(names)
        orderItem[names] = price

for j in orderItem.items():
    print(*j)
