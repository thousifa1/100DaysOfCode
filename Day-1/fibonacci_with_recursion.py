import sys,time

def fib(n):
    if (n==2) or (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2) 

startime=time.time()
b=int(sys.argv[1])
a=fib(b)
elapsedtime=time.time()-startime
print (a)
print ("Time Executed is : "+str(elapsedtime) )
