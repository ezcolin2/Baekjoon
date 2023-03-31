import sys
import copy
input=sys.stdin.readline
n, m, r = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)] #배열
commands=list(map(int, input().split())) #연산
rr=[ #5, 6번 연산을 해결하기 위한 구간
    [[i for i in range(n//2)], [i for i in range(m//2)]],
    [[i for i in range(n//2)], [i for i in range(m//2, m)]],
    [[i for i in range(n//2, n)], [i for i in range(m//2, m)]],
    [[i for i in range(n//2, n)], [i for i in range(m//2)]]
    
]
for i in commands:
    if i==1:
        arr=arr[::-1]
    elif i==2:
        n=len(arr)
        m=len(arr[0])
        for j in range(n):
            arr[j]=arr[j][::-1]
    elif i==3:
        n=len(arr)
        m=len(arr[0])
        temp2=[]
        for j in range(m):
            temp=[]
            for k in range(n-1, -1, -1):
                temp.append(arr[k][j])
            temp2.append(temp)
        arr=temp2
    elif i==4:
        n=len(arr)
        m=len(arr[0])
        temp2=[]
        for j in range(m-1, -1, -1):
            temp=[]
            for k in range(n):
                temp.append(arr[k][j])
            temp2.append(temp)
        arr=temp2
    elif i==5:
        n=len(arr)
        m=len(arr[0])
        rr=[ #5, 6번 연산을 해결하기 위한 구간
            [[i for i in range(n//2)], [i for i in range(m//2)]],
            [[i for i in range(n//2)], [i for i in range(m//2, m)]],
            [[i for i in range(n//2, n)], [i for i in range(m//2, m)]],
            [[i for i in range(n//2, n)], [i for i in range(m//2)]]

        ]

        arr_copy=copy.deepcopy(arr)
        for j in range(4):
            for k in range(n//2):
                for l in range(m//2):
                    arr[rr[j][0][k]][rr[j][1][l]]=arr_copy[rr[(j+3)%4][0][k]][rr[(j+3)%4][1][l]]
    elif i==6:
        n=len(arr)
        m=len(arr[0])
        rr=[ #5, 6번 연산을 해결하기 위한 구간
            [[i for i in range(n//2)], [i for i in range(m//2)]],
            [[i for i in range(n//2)], [i for i in range(m//2, m)]],
            [[i for i in range(n//2, n)], [i for i in range(m//2, m)]],
            [[i for i in range(n//2, n)], [i for i in range(m//2)]]

        ]

        arr_copy=copy.deepcopy(arr)
        for j in range(4):
            for k in range(n//2):
                for l in range(m//2):
                    arr[rr[j][0][k]][rr[j][1][l]]=arr_copy[rr[(j+1)%4][0][k]][rr[(j+1)%4][1][l]]




for i in arr:
    for j in i:
        print(j, end=' ')
    print()
