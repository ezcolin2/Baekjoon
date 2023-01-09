li=[-1]*26
s = list(map(ord, input()))
for i in range(len(s)):
    if li[s[i]-ord('a')]==-1:
        li[s[i]-ord('a')]=i
for i in li:
    print(i, end=" ")