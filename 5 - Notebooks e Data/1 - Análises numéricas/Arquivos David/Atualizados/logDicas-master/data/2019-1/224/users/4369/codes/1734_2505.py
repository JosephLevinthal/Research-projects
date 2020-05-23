from math import*
x=eval(input("angulo x: "))
k=float(input("numero k de termos de serie: "))
senx=0
c=0
i= 1
while c<k:
	sinal= (-1)**c
	senx= senx+ sinal*(((x**i))/factorial(i))
	c= c+1
	i= i+2
print(round(senx, 10))
