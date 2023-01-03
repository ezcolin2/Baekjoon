n = int(input())
for i in range(n):
    print(" "*i, end="")
    m = 2*n-1-2*i
    print("*"*m)
for i in range(1, n):
    print(" "*(n-i-1), end="")
    m = 2*i+1
    print("*"*m)
