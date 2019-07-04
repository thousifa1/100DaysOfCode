testcases=int(input())

def fib_mem(n):
    if (arr[n]==-1):
        p=fib_mem(n-1)+fib_mem(n-2)
        arr[n]=p
        return p
    else:
        return arr[n]


for i in range(testcases):
    b=int(input())
    arr = [-1] * (b+1)
    arr[1]=1
    arr[2]=1
    a=fib_mem(b)
    print (a)
