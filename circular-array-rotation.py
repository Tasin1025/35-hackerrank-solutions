def solve(a, n, k):
    b = []
    k %= n
    for i in range(n - k, n):
        b.append(a[i])
    for i in range(n - k):
        b.append(a[i])
    return b



n, k, q = map(int, input().split())
a = list(map(int, input().split()))
list_ans = solve(a, n, k)
for _ in range(q):
    idx = int(input())
    print(list_ans[idx])