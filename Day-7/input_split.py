testcases=int(input())
a=[]
for i in range(testcases):
    b=input()
    a=b.split(" ")
    a = list(dict.fromkeys(a))
    for i in a:
        print ( i,end=" ")
