#anju
i,r=map(int,input().split())
a=0
for n in range(i,r+1):
    if n == 2 or n == 3 or n == 5 or n == 7:
        a=a+1
    elif (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0) and (n != 1) and n > 0:
        a=a+1
print(a)