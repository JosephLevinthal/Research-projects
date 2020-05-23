po = int(input("quantidades de peca de ouro:"))
n = input("nome da arma:")
f = int(input("fator de sucesso:")) #dado

if ((po >= 100) and (n == "ESPADA") and (f <= 10) and (f >= 1)):
	d = f * 10
	print(d)
elif ((po >= 30) and (n == "MACHADO") and (f<=10) and (f>=1)):
	d = f + 3
	print(d)
elif ((po >= 50) and (n == "MARRETA") and (f <= 10) and (f >= 1)):
	d = f + 5
	print(d)
elif((po >= 100) or(po >= 50) or (po >= 30) and (f < 1) or (f > 10)):
	print("Entrada invalida")
else:
	print("PO insuficiente")