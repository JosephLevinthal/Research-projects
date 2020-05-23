from math import*
x=eval(input("insira o angulo: "))
k= int(input("insira o numero k de termos: "))
s=0
i=1
h=0
snl=+1
while h<k:
	s=s+snl*((x**i)/factorial(i))
	i=i+2
	h=h+1
	snl=-1*snl
print(round(s,10))