numero = int(input("digite numero: "))

perfeito = 0
cont = numero

while(cont > 1):
	if(numero % cont == 0):
		print(numero // cont)
		perfeito = perfeito + (numero // cont)
	cont = cont - 1

if(numero == perfeito):
	print("PERFEITO")
else:
	print("NAO PERFEITO")