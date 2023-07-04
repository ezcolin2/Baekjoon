import sys
input=sys.stdin.readline
short_ipv6=input().rstrip() # 축약 ipv6 
origin_ipv6=[] # 원본 ipv6
arr=short_ipv6.split(':')
zero_group_num=9-len(arr) # 0000 개수
res=[]
already_zero=False # 0으로만 이루어진 그룹 추가 여부
for idx, i in enumerate(arr):
    if i=='' and (idx==0 or idx==7): # 콜론이 가장 처음 혹은 마지막에 붙어 있으면
        res.append('0000')
    elif i=='' and not already_zero: # 0으로만 이루어진 그룹일 경우
        for i in range(zero_group_num): # '0000'으로 채우기
            res.append('0000')
            already_zero=True
    else:
        res.append(i.zfill(4))
print(':'.join(res))