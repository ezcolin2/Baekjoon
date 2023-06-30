import sys
number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def to_english(n): # 숫자를 영어로 바꿈
    temp=''
    while True:
        if n==0:
            break
        temp=number[n%10]+' '+temp
        n=n//10
    return temp
input=sys.stdin.readline
arr=[] # 정렬을 위해서 (영어, 숫자) 담을 배열
n, m = map(int, input().split())
for num in range(n, m+1):
    arr.append((to_english(num), num))
arr.sort()
for idx, i in enumerate(arr):
    print(i[1], end=' ')
    if idx%10==9: # 10번째마다 개행 
        print()