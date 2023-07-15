# 백준 12970
# 그리디
import sys
input=sys.stdin.readline
n, k = map(int, input().split())
s=['B']*n
cnt=0 # (A, B) 쌍의 수
# 불가능한 경우 골라내기
max_cnt=0 # 가장 큰 (A, B)쌍의 개수 
for i in range(n//2+1):
    max_cnt=max(max_cnt, i*(n-i))
if max_cnt<k: # 못 만드는 경우
    print(-1)
    exit()
while cnt!=k:
    idx=n-1 # 뒤에서부터 A 옮기기
    cnt-=s.count('A') # 가장 마지막 B를 A로 바꾸면 앞 A 개수만큼 (A, B)쌍의 수가 줄어듦
    if cnt==k:
        break
    s[idx]='A' # 가장 뒤 B를 A로 변경
    while idx>0 and s[idx-1]=='B'and cnt!=k:
        # A를 한 칸 앞으로 땡겨옴
        s[idx]='B' 
        idx-=1
        s[idx]='A'
        cnt+=1
if s.count('A')==0:
    s[-1]='A'
print(''.join(s))
