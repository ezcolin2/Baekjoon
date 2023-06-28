import sys
from collections import Counter
input=sys.stdin.readline
trees=[]
total=0
while True:
    temp=input().rstrip()
    if temp=='':
        break
    trees.append(temp)
    total+=1
trees.sort()
dict=Counter(trees)
for key, value in dict.items():
    print(key, f"{(value/total)*100 :.4f}")