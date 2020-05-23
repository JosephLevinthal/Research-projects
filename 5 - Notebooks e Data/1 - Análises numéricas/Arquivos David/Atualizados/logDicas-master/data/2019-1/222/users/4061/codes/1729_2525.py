numero = int(input("digite numero: "))

divisores = 0
cont = numero

while(cont > 0):
	if(numero % cont == 0):
		print(numero // cont)
		divisores = divisores + 1
	cont = cont - 1

if(divisores < 2):
	print(divisores, " divisor")
else:
	print(divisores, " divisores")
