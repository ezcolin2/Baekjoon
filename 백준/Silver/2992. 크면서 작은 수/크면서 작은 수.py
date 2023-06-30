import sys
input=sys.stdin.readline
number=[0]*10 # 각 숫자 등장 횟수
s=input().rstrip()
for i in s:
    number[int(i)]+=1
res=[]
for i in range(len(s)): # i번째를 더 큰 수로 바꿈
    temp_arr=number.copy()
    temp=''
    for j in range(i):
        temp+=s[j]
        temp_arr[int(s[j])]-=1
    for j in range(int(s[i])+1, 10): # 더 큰 수가 있는지 확인
        if temp_arr[j]>0: # 더 큰 수 중 작은 값 발견
            temp_arr[j]-=1
            temp+=str(j)
            break
    # if len(temp)==i: # 더 큰 수를 발견하지 못했다면
    #     temp+=ss[]
    #     temp_arr[int(s[i]+1)]-=1
    # 아래 과정은 더 큰 수 중 가장 작은 값을 구하는 과정
    for j in range(10):
        while temp_arr[j]>0: # 만약 수를 발견한다면 다 넣음
            temp+=str(j)
            temp_arr[j]-=1
    if temp>s:
        res.append(temp) # 경우의 수 넣어놓고 가장 작은 값 구하기
if len(res)==0: # 없음 
    print(0)
else:
    print(min(res))

