from numpy import*
a=array(eval(input("presentes:")))
b=array(eval(input("faltantes:")))
i=0
x=1
while(b[i]!=max(b)):
	i=i+1
	x=x+1
print(x)