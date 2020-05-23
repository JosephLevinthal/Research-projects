opc = input("Lanche(L) ou Salgado(S): ")
qls = int(input("Quantidade de lanches ou salgados: "))
qr = int(input("Quantidades de refrigerantes: "))
l = 5.00
s = 3.50
r = 4.00
if(opc.upper() == "L"):
	valor = qls*l + qr*r
if(opc.upper() == "S"):
	valor = qls*s + qr*r
	
print(round(valor,2))