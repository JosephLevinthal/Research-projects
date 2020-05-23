from numpy import *
string=input("digite algo").upper()
v=0
c=0
for ch in string:
	if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
		v=v+1
	else:
		c=c+1
print(v)
print(c)