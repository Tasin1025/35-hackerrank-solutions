def miniMaxSum(arr):
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp = 0
        for j in range(i,i+4):
            temp = temp + arr[j]
        hold[i] = temp
    
    print(hold[0],hold[-1])



arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)