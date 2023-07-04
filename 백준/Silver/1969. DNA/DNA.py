import sys
import heapq
from collections import Counter
input=sys.stdin.readline
n, m = map(int, input().split())
arr=[input().rstrip() for _ in range(n)]
min_dna='' # hamming distance가 가장 작은 dna
distance_sum=0 # hamming distance의 합
for i in range(m):
    temp=[] # 같은 열 원소 배열
    for j in range(n):
        temp.append(arr[j][i])
    c=Counter(temp) 
    sorted_counter=sorted(c.items(), key=lambda x : (-x[1], x[0]))
    nucletide, common = sorted_counter[0]
    min_dna+=nucletide
    distance_sum+=n-common
print(min_dna)
print(distance_sum)