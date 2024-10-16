n, m = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[0]
prefix_sum = [0]*(n+2)
for _ in range(m):
    a, b, k = map(int, input().split())
    prefix_sum[a] += k
    prefix_sum[b+1] -= k
for i in range(1, n+1):
    prefix_sum[i] += prefix_sum[i-1]
for i in range(1, n+1):
    print(arr[i] + prefix_sum[i], end=' ')
