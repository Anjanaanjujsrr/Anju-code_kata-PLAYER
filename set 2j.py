#anju
x=input()
y=''
for i in x:
    if i=="X":
        y+="A"
    elif i=="Y":
        y+="B"
    elif i=="Z":
        y+="C"
    else:
        y+=chr(ord(i)+3)
print(y)