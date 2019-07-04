testcases=int(input())
a=[]
for i in range(testcases):
    a.append(int(input()))
    maximum=max(a)

def factorial(n):
    if (arr[n]==-1):
        p=n*factorial(n-1)
        arr[n]=p
        return p
    else:
        return arr[n]


arr = [-1] * (maximum+1)
arr[0]=1
arr[1]=1
if maximum>1:
    arr[2]=2
factorial(maximum)

for i in a:
    print (arr[i])