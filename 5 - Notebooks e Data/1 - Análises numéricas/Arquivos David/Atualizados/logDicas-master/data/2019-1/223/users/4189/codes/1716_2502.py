from math import sqrt
n=int(input("Quantidades de termos: "))
r=0
expoente=0
denominador=1
cont=0
sinal=1
while(cont<n):
	r=r+sqrt(12)*(sinal*(1/(denominador*(3**expoente))))
	sinal=sinal*(-1)
	denominador=denominador+2
	expoente=expoente+1
	cont=cont+1
print(round(r, 8))