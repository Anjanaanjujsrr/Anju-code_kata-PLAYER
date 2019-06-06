#anju
a=int(input())
b=[]
for x in range(2,a+1):
  if(a%x==0):
    o=0
    for i in range(1,x+1):
      if(x%i==0):
        o=o+1
    if(o==2):
      b.append(x)
for i in range(0,len(b)):
  if(i==len(b)-1):
    print(b[i])
  else:
    print(b[i],end=(' '))