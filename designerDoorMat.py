n , m = [int(i) for i in input().split()]
temp= ".|."
odd= [ x for x in range(n) if x%2==1]
middle= n//2
for i in range(n):
    if i < middle:
        pattern = temp*odd[i]
        print(pattern.center(m,"-"))
    elif i > middle:
        middle-=1
        pattern = temp*odd[middle]
        print(pattern.center(m, "-"))
    else:
        print("WELCOME".center(m, "-"))
