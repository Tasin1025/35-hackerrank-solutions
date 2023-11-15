def birthdayCakeCandles(ar):
    c = 0
    temp = ar[0]
    for i in range(1,len(ar)):
        if ar[i] > temp:
            temp = ar[i]
    for i in range(0,len(ar)):
        if ar[i] == temp:
            c = c + 1
    return c

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(ar)

print(result)