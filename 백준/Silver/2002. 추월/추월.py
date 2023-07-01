import sys
input=sys.stdin.readline
n=int(input())
before=[input().rstrip() for _ in range(n)] # 들어가기 전 순서 
after=dict() # 나온 후 순서
# for i in range(n):
#     before[input().rstrip()] = i
for i in range(n):
    after[input().rstrip()] = i
cnt=0 # 추월 차량 수
# numbers=before.keys()
for i in range(n):
    # 차례대로 앞 순서 조사
    current_num = before[i] # 현재 조사 중인 차량 번호 
    for j in range(i):
        before_num = before[j]
        if after[before_num]>=after[current_num]: # 원래 앞에 있던 차량이 뒤에 있다면
            cnt+=1
            break
print(cnt)