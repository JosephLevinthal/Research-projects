from math import*
x = eval(input("Digite o angulo:"))
k = int(input("O num k de termos:"))
t = 0
sen=0
while (t<k):
	if(t%2!=0):
		sen = sen + x**(1+2*t)/factorial(1+2*t)
		t =t+1
	else:
		sen = sen-x**(1+2*t)/factorial(1+2*t)
		t = t+1
print(round((-1)*sen,10))
