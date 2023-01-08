li = [(i+1) for i in range(10000)]
r=[]
def d(n):
    if(n>10000): return
    res=n
    for i in str(n):
        res+=int(i)
    r.append(res)
    d(res)
for i in range(1,10001):
    d(i)
for i in sorted(set(li)-set(r)):
    print(i)