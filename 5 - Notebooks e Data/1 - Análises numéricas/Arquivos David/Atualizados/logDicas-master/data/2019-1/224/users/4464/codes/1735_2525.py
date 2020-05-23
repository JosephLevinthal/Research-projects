n = int(input("insira o numb: "))

cont = 1
div = 0

while (cont <= n):
	if(n % cont==0):
		print(cont)
		div = div + 1
	cont = cont + 1
	
print(div, "divisores")