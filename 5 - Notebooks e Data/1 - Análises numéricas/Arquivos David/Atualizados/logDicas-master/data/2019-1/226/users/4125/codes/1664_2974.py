x = int(input("digite em gramas o acai: "))
x1 = int(input("digite quantos salgados vc quer: "))
x2 = float(input("quanto de dinheiro: "))
y = 24
salgado = 3
x4 = (x/1000)*y + x1*salgado
if (x2 < x4):
	print(round(x4,2))
	print("Nao")
	
else:
	print(round(x4,2))
	print("Sim")