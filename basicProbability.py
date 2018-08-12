import math
n = int(input())
a= list(range(1,n+1))
b= list(range(1,n+1))
eventAoutCome= 0
for i in range(len(a)):
    temp1 = a[int(i)]
    for j in range(len(b)):
        temp2 = b[int(j)]
        if temp1+temp2 <=9:
            eventAoutCome += 1
print(eventAoutCome/math.pow(n,2) == 5/6)
