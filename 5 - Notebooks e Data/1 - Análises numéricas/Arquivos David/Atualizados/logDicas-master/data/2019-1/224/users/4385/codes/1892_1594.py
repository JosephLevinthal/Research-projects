from numpy import*
v=array(eval(input("digite: ")))
s=0
b=1
for i in range(size(v)):
	s=s+(v[i]*b)
	b=b+1
print(s)