valor = int(input("Numeros de termos: "))

cont = 1
apx = 3

while (cont < valor):
	x = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	apx = apx + (-1) ** (cont + 1) * 4 / x 
	cont =  cont + 1
	
print(round(apx,8))
