QT = int(input("Quantidade de tambaqui: "))
PCT = float(input("percy de crecimento anual de tambaqui: "))
Tirados = int(input("insira quantos tambaquis sao tirados: "))

A = QT
cont = 0


while (A > 0 and A < 12000):
	A = A + ((A*PCT)/100) - Tirados
	cont = cont + 1
if (A <= 0):
	print("EXTINCAO")
	print(cont)
else:
	print("LIMITE")
	print(cont)
