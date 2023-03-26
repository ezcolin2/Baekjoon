import sys
from collections import deque
input=sys.stdin.readline
arr=[int(input()) for _ in range(9)]
arr.sort()
temp=sum(arr)-100 #일곱 난쟁이가 아닌 두 난쟁이의 키 합
con=False
for i in range(9):
    if con:
        break
    for j in range(i+1, 9):
        if arr[i]+arr[j]==temp:
            arr_i=arr[i]
            arr_j=arr[j]
            arr.remove(arr_i)
            arr.remove(arr_j)
            con=True
            break
for i in arr:
    print(i)