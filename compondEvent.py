from functools import reduce
color= [tuple(map(int, input().split())) for _ in range(3)]
redBall= [i[0] for i in color]
blackBall= [i[1] for i in color]
sum= [sum(i) for i in color]
product= reduce((lambda x,y: x*y), sum)
RRB = redBall[0:2]+blackBall[2:]
RBR = redBall[0:1]+blackBall[1:2]+redBall[2:]
BRR= blackBall[0:1]+redBall[1:]
dominater1= reduce((lambda x,y: x*y), RRB)
dominater2= reduce((lambda x,y: x*y), RBR)
dominater3= reduce((lambda x,y: x*y), BRR)


pA= dominater1/product
pB = dominater2/product
pC = dominater3/product
print((pA+pB+pC) == 17/42)
