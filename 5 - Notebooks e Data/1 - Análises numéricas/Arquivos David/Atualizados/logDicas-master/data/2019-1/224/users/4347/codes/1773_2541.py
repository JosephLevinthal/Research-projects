from numpy import*
p=array(eval(input("coodernadas p: ")))
y=array(eval(input(" coodernadas q: ")))
h=0
a=0
while(len(p)>h):
	z=((p[h]-y[h])**2)+ a
	a=z
	h=h+1
print(round(z**0.5,4))