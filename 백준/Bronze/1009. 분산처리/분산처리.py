T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        print(a if b % 2 == 1 else (6 if a == 4 else 1))
    else:
        b = b % 4
        if b == 0:
            b = 4
        result = pow(a, b) % 10
        print(result)