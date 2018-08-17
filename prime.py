def is_prime(a):
    return all(a % i for i in range(2, a))


n = int(input())
for _ in range(3):
    x = int(input())
    svar = is_prime(x)
    if svar:
        print("Prime")
    else:
        print("Not prime")
