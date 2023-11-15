def migratoryBirds(arr):
    
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratoryBirds(arr)
print(str(result) + '\n')
