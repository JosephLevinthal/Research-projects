PO = float(input("qtd de pecas de ouro: "))
n = input("nome? (ESPADA/MACHADO/MARRETA)" )
f = int(input("valor: (1/2/3/4/5/6/7/8/9/10) "))

if(f >= 1) and (f <= 10) and (n == "ESPADA") or (n == "MACHADO") or (n == "MARRETA"):
	if(n == "ESPADA") and (PO >= 100):
		d1 = f*10
		print(d1)
	elif(n == "MACHADO") and (PO >= 30):
		d2 = f + 3
		print(d2)
	elif(n == "MARRETA") and (PO >= 50):
		d3 = f + 5
		print(d3)
	else: 
		print("PO insuficiente")
else: 
	print("Entrada invalida")