def aVeryBigSum(ar):
    x=0
    for i in range(0,len(ar)):
        x= x + ar[i]
    return x


ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)