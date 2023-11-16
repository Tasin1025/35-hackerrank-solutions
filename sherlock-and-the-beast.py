T = int(input())
for i in range(T):
    k = int(input())
    n1 = k
    n2 = 0
    done = False
    while n1 >= 0:
        if n1%3 == 0 and n2%5 == 0:
            for j in range(n1):
                print('5',end='')
            for j in range(n2):
                print('3',end='')
            print()
            done = True
            break
        n1 -= 1
        n2 += 1
    if not done:
        print(-1)