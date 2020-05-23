from numpy import*
string=input("digite o nome:")
v=0
for i in string:
	if(i!="a" and i!="e" and i!="i" and i!="o" and i!="u"):
		v=v+1
print(len(string)-v)
print(v)
	
