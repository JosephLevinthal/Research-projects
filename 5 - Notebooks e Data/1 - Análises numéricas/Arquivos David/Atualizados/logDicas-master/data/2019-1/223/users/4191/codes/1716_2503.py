n=int(input("valor de n: "))
cont=0
r=0
sinal=1
denominador=1

while(cont<n):
	r=r+(sinal*4/denominador)
	sinal=sinal*(-1)
	denominador=denominador+2
	cont=cont+1

print(round(r, 8))