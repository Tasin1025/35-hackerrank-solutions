x = int(input())
n = int(input())

def rec(x,n,start):
    count = 0 
    for i in range(start,x):
        ans = x-i**n
        if ans == 0:
            count += 1
        if ans> 0 :
            count += rec(ans,n,i+1)
        if ans<0:
            continue   
    return count
    
print(rec(x,n,1))
