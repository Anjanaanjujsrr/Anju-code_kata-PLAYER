#anju
a,b=map(int,input().split())
Q=a*b
M=[]
for i in range(1,Q+1):
    if i%a==0 and i%b==0:
        M.append(i)
print(min(M))