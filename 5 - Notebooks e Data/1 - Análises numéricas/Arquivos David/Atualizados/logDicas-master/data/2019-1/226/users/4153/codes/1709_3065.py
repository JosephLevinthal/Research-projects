t = input("Insira o tipo do ataque: ").upper()# tipo de ataque
n = int(input("Insira o valor sorteado: "))   # valor sorteado pelo dado
r = int(input("Insira o numero de turnos: ")) # numero de turnos

if((t != "CAUDA") and (t != "CUSPE") and (t != "PATADA") or (n < 1) or (n > 4)):
	print("Entrada invalida")
elif(t == "CAUDA"):
	d = n * r
	print(d)
elif(t == "CUSPE"):
	d = 2 * n * r
	print(d)
elif(t == "PATADA"):
	d = 2 * n - 5 * r
	print(d)