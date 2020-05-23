r=input("digite o resultado: ")
a=0
b=0
c=0
while(r.upper()!="X"):
	if(r.upper()=="V"):
		soma=a+3
		a=soma
	if(r.upper()=="E"):
		somb=b+2
		b=somb
	if(r.upper()=="D"):
		somc=c+1
		c=somc
	r=input("digite o resultado: ")
print(a)
print(b)
print(c)
		