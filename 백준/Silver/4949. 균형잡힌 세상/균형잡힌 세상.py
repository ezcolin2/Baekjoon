import sys
s=sys.stdin.readline().strip('\n')
while s!='.':
    stack = []
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='[':
            stack.append(s[i])
        elif s[i]==')':
            if len(stack)==0:
                stack.append(s[i])
                break
            if stack[-1]=='(':
                stack.pop()
            elif stack[-1]=='[':
                break
        elif s[i]==']':
            if len(stack)==0:
                stack.append(s[i])
                break
            if stack[-1]=='[':
                stack.pop()
            elif stack[-1]=='(':
                break
    if len(stack)!=0:
        print("no")
    else:
        print("yes")
    s=sys.stdin.readline().strip('\n')