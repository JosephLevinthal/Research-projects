n=int(input("Quantidades de termos: "))
sinal=1
numerador=2
cont=1
result=3
denominador=4

while(cont<n):
	result=result+(sinal*(4/(numerador*(numerador+1)*(numerador+2))))
	sinal=sinal*(-1)
	numerador=numerador+2
	cont=cont+1

	
	
	
print(round(result, 8))