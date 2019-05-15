import sys,time

def fib(n):
    if (n==2) or (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2) 

def fib_mem(n):
    if (arr[n]==-1):
        p=fib_mem(n-1)+fib_mem(n-2)
        arr[n]=p
        return p
    else:
        return arr[n]



startime=time.time()
b=int(sys.argv[1])
arr = [-1] * (b+1)
arr[1]=1
arr[2]=1
a=fib_mem(b)
elapsedtime=time.time()-startime
print (a)
print ("Time Executed is : "+str(elapsedtime) )
""" for e in arr:
    print("The Element  in array are "+str(e)) """