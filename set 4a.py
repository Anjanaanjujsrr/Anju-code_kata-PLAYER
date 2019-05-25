#anju
K=input()
for i in K:
	A=K.count('(')
	B=K.count(')')
if A==B:
	print("yes")
else:
	print("no")