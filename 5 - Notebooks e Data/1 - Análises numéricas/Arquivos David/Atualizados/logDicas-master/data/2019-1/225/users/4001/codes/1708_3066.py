V = int(input("Qtd inicial de vida: "))
var1 = int(input("var1: "))
var2 = int(input("var2: "))
var3 = int(input("var3: "))
N = var1 + var2 + var3
if (V < 0) or (var1 < 1) or (var1 > 12) or (var2 < 1) or (var2 > 12) or (var3 < 1) or (var3 > 12):
	print("Entrada invalida")
else:
	if(V - 10 * N <= 0):
		print(0)
		print("MORTO")
	else:
		print(V - 10 * N)
		print("VIVO")
	