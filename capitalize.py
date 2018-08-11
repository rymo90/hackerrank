s= input()
temp= s.split(" ")
svar= []
for i in temp:
    if len(i)==0:
        svar.append("")
    else:
        svar.append(i[0].upper()+i[1:])
print(" ".join(svar))
