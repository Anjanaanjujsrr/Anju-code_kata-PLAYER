#anju
string = input()
string = list(string)
for i in range(0,len(string),2):
    string[i], string[i+1] = string[i+1], string[i]  
print( ''.join(string))