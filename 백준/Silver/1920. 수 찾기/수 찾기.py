import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int, input().split()))
m=int(input())
li2=list(map(int, input().split()))
li.sort()
def binary_search(x, low, high):
    global li
    mid=(low+high)//2
    if high<low:
        return 0
    if li[mid]==x:
        return 1
    if li[mid]<x:
        return binary_search(x, mid+1, high)
    if li[mid]>x:
        return binary_search(x, low, mid-1)

for i in li2:
    print(binary_search(i, 0, len(li)-1))