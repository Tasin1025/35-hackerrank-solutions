t = int(input())
for i in range(t):
    part = list(map(int, input().split(' ')))
    print((part[1] + part[2] - 2) % part[0] + 1)