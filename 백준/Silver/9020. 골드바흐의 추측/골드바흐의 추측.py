prime = [True]*10001
prime[0:2]=[False,False]
for i in range(2, 10001):
    for j in range(i+i, 10001, i):
        prime[j]=False
t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(n//2, 10000):
        if prime[n-i] and prime[i]: #둘 다 소수라면
            print(n-i, i)
            break