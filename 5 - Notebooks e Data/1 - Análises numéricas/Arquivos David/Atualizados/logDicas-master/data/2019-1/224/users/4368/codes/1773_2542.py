from numpy import*
x=array(eval(input("passageiros que entram: ")))
y=array(eval(input("passageiros que saem: ")))
h=0
a=0
while(len(x)>h):
	z=a+(x[h]-y[h])
	a=z
	h=h+1
print(z)