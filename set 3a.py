#anju
a,b=map(int,input().split(" "))
x,y=map(int,input().split(" "))
s,t=map(int,input().split(" "))
if a==x==s:
	print("yes")
elif b==y==t:
	print("yes")
elif a==b and x==y and s==t:
	print("yes")
else:
	print("no")