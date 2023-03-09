import sys
input = sys.stdin.readline
n=int(input())
arr=[True for _ in range(n+1)] #편하게 1부터 계산하기 위함
for i in range(2, n+1): #에라토스테네스의 체로 걸러냄
    for j in range(i*2, n+1, i):
        arr[j]=False
primes = [] #소수들을 보관할 리스트
for i in range(2, n+1):
    if arr[i]: #소수라면 추가
        primes.append(i)
left=0
right=0
subtotal=2 #부분합
cnt = 0 #조건을 만족하는 부분합의 개수
size=len(primes) #소수들을 모아둔 리스트의 길이
while left<size and right<size:
    if subtotal==n: #문제의 조건을 만족
        cnt+=1
        subtotal-=primes[left]
        left+=1
        right+=1
        if right<size:
            subtotal+=primes[right]
        
    elif subtotal<n:
        right+=1
        if right<size:
            subtotal += primes[right]
    else:
        subtotal -= primes[left]
        left+=1
print(cnt)