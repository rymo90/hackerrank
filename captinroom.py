k = int(input())
t = input().split()
num= len(t)//k
s = list(set(t))
dic = {}
for i in range(len(s)):
    dic[s[i]] = 0
for j in range(len(t)):
    dic[t[j]] += 1
for key in dic.keys():
    if dic[key] == 1:
        print(key)
        break
