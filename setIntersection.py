input()
english = set(map(int, input().split()))
input()
french = set(map(int, input().split()))
print(len(french.intersection(list(english))))
