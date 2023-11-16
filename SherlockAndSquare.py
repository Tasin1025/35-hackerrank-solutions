t = int(input())
for _ in range(t):
    n = int(input())
    result = 2 * (1 + pow(2, n, 10**9 + 7)) % (10**9 + 7)
    print(result)
