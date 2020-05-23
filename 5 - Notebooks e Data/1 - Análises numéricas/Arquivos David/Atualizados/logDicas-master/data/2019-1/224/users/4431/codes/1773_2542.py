from numpy import*
x=array(eval(input("Passageiros que entram: ")))
y=array(eval(input("Passageiros que saem: ")))
h=0
a=0
while(len(x)>h):
	z=a+(x[h]-y[h])
	a=z
	h=h+1
print(z)	