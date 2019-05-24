#anju
a,b=list(map(str,input().split()))
g=0
for i in range(0,len(a)):
    if a[i]!=b[i]:
        g=g+1
if g==1:
    print("yes")
else: print("no")