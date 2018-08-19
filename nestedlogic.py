d, m, y = map(int, input().split())
d2, m2, y2 = map(int, input().split())
diffDay = d > d2
diffMonth = m > m2
diffYear = y > y2
fine = 0
track = ""
if diffYear:
    fine = 1000

else:
    if diffMonth and y == y2:
        fine = 500*(abs(m-m2))

    else:
        if diffDay and m == m2:
            fine = 15*(abs(d-d2))

print(fine)
