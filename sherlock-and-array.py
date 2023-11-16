for i in range(int(input())):
    n = int(input())
    a = [int(b) for b in input().split()]
    s = sum(a)
    count = 0
    for j in range(n):
        if 2*count == s-a[j]:
            print("YES")
            break
        count += a[j]
    else:
        print("NO")
                       