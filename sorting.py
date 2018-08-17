s = int(input())
a = list(map(int, input().strip().split(' ')))


def bubbleSort(a):
    swap = 0
    for passnum in range(len(a)-1, 0, -1):
        for i in range(passnum):
            if a[i] > a[i+1]:
                swap += 1
                a[i], a[i+1] = a[i+1], a[i]
    return swap


swap = bubbleSort(a)
print("Array is sorted in", swap, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a)-1])
