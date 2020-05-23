a = int(input("PO: "))
b = input("Armadura: ").upper()
d = int(input("Valor do dado: "))

if (a >= 200) and (b == "INTEIRA"):
	x1 = 30 * d - 20 
elif (a >= 50) and (b == "MALHA"):
	x1 = 15 * d -1 
elif (a >= 100 ) and (b == "PLACA"):	
	x1 = 20 * d - 18
elif (a <= 200)	and (b == "INTEIRA") or (a <= 50) and (b == "MALHA") or (a <= 100) and (b == "PLACA"):
	x1 = "PO insuficiente"
print(x1)