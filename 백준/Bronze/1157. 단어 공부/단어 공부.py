alpha = [0]*26
s=input()
for i in s:
    if 'a'<=i<='z':
        alpha[ord(i)-ord('a')]+=1
    else:
        alpha[ord(i)-ord('A')]+=1
m=max(alpha)
li=[]
for i in alpha:
    if i==m:
        li.append(i)
if len(li)>1:
    print('?')
else:
    print(chr(ord('A')+alpha.index(m)))