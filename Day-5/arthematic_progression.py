#https://practice.geeksforgeeks.org/problems/series-ap/0/?track=interview-mathematical&batchId=117
testcases=int(input())
for i in range(testcases):
    c=input()
    a,b=c.split()
    d=(int(b))-(int(a))
    n=int(input())
    n=n-1
    print (int(a)+n*d)