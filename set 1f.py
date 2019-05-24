#anju
a,b=list(map(str,input().split()))
s1=len(set(a)) 
s2=len(set(b))
if s1==s2:
	print ("yes") 
else:
	print ("no") 