t=int(input())
for _ in range(t):
    n, a = input().split()
    li=list(map(lambda x:x*int(n), a))
    res=""
    for i in li:
        res+=i
    print(res)

    
