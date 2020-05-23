from numpy import*
x=array(eval(input("Digite as coodernadas p: ")))
y=array(eval(input("Digite as coodernadas q: ")))
h=0
a=0
while(len(x)>h):
	z=((x[h]-y[h])**2)+ a
	a=z
	h=h+1
print(round(z**0.5,4))	

	