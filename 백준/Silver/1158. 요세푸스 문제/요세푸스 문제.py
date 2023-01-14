import sys 
k, n =map(int, sys.stdin.readline().split())
li=[i for i in range(1, k+1)]
idx = 0
print('<', end = '')
while len(li)>0:
    idx=(idx+n-1)%len(li)
    if len(li)!=1:
        print(li.pop(idx),end = ', ')
    else:
        print(li.pop(idx), end = '')
print('>', end = '')
