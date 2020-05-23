po=int(input("qtd de gold: "))
a=input("armadura: ")
d=int(input("numero de 1 a 8: "))
if (po==0):
		print("Entrada invalida")
elif (po>=200) and (a=="INTEIRA"):
		print(30*d-20)
elif (po>=50) and (a=="MALHA"):
		print(15*d-1)
elif (po>=100) and (a=="PLACA"):
		print(20*d-18)
else:
		print("PO insuficiente")