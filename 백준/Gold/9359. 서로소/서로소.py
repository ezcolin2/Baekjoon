import sys
from itertools import combinations
input=sys.stdin.readline
t=int(input())
for p in range(t):
    a, b, n = map(int, input().split())
    temp=n 
    prime_num = [] #소수
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            prime_num.append(i)
            while temp%i==0:
                temp//=i
    if temp!=1:
        prime_num.append(temp)
     
     #소수 구하기 완료
    temp_a=a-1
    temp_b=b


    for i in range(1, len(prime_num)+1):
        for j in combinations(prime_num, i):
            m=1
            for k in j:
                m*=k
            if i%2:
                temp_a-=(a-1)//m
                temp_b-=b//m
            else:
                temp_a+=(a-1)//m
                temp_b+=b//m
    print(f'Case #{p+1}: {temp_b-temp_a}')

     

