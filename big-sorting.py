
def bigSorting(unsorted):
    return sorted(unsorted,key=lambda x: (len(x), x))
    

n = int(input())

unsorted = []

for i in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

result = bigSorting(unsorted)

print('\n'.join(result))
print('\n')

