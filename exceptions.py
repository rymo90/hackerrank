n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as identifier:
        print("Error Code:", identifier)
