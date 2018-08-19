import re

names = []
n = int(input())
for _ in range(n):
    s = input().split()
    nameId = "".join(s[0])
    emailId = re.findall(r'(.+)@gmail.com', "".join(s[1]))
    if emailId:
        names.append(nameId)
for i in sorted(names):
    print(i)
