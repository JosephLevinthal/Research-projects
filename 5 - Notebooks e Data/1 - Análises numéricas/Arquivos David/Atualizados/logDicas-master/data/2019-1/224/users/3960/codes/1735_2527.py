n = int(input("Numero inteiro positivo: "))

cont = 1
div = 0

while(cont < n):
	if(n % cont == 0):
		div = div + cont
		print(cont)
	cont = cont + 1
	
if(div == n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")