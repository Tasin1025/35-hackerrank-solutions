
import math

def squares_between(a, b):
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count



tcount = int(input())

for i in range(tcount):
    a, b = tuple(int(pair) for pair in input().split())
    print(squares_between(a, b))