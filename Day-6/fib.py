#https://practice.geeksforgeeks.org/problems/last-two-digits-of-fibonacci/0/?track=interview-mathematical&batchId=117
testcases=int(input())
a=[]
for i in range(testcases):
    #lines+=input()+"\n"
    a.append(int(input()))
    maximum=max(a)
if maximum > 300:
    maximum=300

def fib_mem(n):
    if (arr[n]==-1):
        p=fib_mem(n-1)+fib_mem(n-2)
        arr[n]=p%100
        return p
    else:
        return arr[n]


arr = [-1] * (maximum+1)
arr[1]=1
if maximum>1:
    arr[2]=1
fib_mem(maximum)

for i in a:
    i=i%300
    print (arr[i])