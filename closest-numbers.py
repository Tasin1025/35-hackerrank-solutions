def minimaldifference(arr):
    minimal = abs(arr[0]-arr[1])
    for i in range(1, len(arr)-1):
        absValue = abs(arr[i]-arr[i+1])
        if absValue < minimal:
            minimal = absValue
    return minimal

def closestNumbers(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    result = []
    minimalDiff = minimaldifference(sorted_arr)
    for i in range(len(arr)-1):
        if abs(sorted_arr[i] - sorted_arr[i+1]) == minimalDiff:
            result.append(sorted_arr[i])
            result.append(sorted_arr[i+1])
    return result

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = closestNumbers(arr)

print(' '.join(map(str, result)))
print('\n')