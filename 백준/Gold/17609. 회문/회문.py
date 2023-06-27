import sys
input=sys.stdin.readline
def is_palindrome(num): #회분 판단 
    return num==num[::-1]

def is_pseudo_palindrome(num): #유사 회문 판단
    left=0
    right=len(num)-1
    cnt=0 #건너뛴 횟수
    for _ in range(len(num)//2):
        if num[left]!=num[right]:
            if num[left+1]==num[right]:
                left+=1
                cnt+=1
            elif num[left]==num[right-1]:
                right-=1
                cnt+=1
            else:
                cnt+=2
        left+=1
        right-=1
    if cnt==1:
        return True
    # return False


    left=0
    right=len(num)-1
    cnt=0 #건너뛴 횟수
    for _ in range(len(num)//2):
        if num[left]!=num[right]:
            if num[left]==num[right-1]:
                right-=1
                cnt+=1
            elif num[left+1]==num[right]:
                left +=1
                cnt+=1
            else:
                cnt+=2
        left+=1
        right-=1
    if cnt==1:
        return True
    return False

    
        

n=int(input())
for _ in range(n):
    temp=list(input().rstrip())
    if is_palindrome(temp):
        print(0)
    elif len(temp)==2 or is_pseudo_palindrome(temp):
        print(1)
    else:
        print(2)
