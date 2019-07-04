from numpy.ma.core import max
testcases=int(input())
a=[]
for i in range(testcases):
    #lines+=input()+"\n"
    a.append(int(input()))

print (max(a))