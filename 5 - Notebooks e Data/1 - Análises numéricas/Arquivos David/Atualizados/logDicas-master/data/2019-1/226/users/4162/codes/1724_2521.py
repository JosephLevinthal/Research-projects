nf= int(input("digite um numero inteiro N maior que zero: "))
s=1
t=0
x=1
y=3
while t<nf:
	t=t+1
	s=s+ x/y
	x=x*(x+1)
	y=y*(y+2)

r=2*s
print(round(r,10))