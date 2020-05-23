from numpy import*
x=array(eval(input("digite as coordenadas q: ")))
y=array(eval(input("digite as coordenadas q: ")))
h=0
a=0
while(len(x)>h):
	z=((x[h]-y[h])**2)+a
	a=z
	h=h+1
print(round(z**0.5,4))