from math import*
x= eval(input("insira um angulo: "))
k= int(input("insira a quantidade de termos: "))
t=1
s=1
snl=-1
i=2
while t<k:
	s=s+snl*((x**i)/(factorial(i)))
	i=i+2
	snl=snl*-1
	t=t+1
r=s
print(round(r,10))