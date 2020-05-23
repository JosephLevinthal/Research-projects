po = int(input("QTD OURO:"))
a = input("ARMADURA:")
d = int(input("destreza:"))
b = a.upper()	  
if(b != "MALHA"):
	print("Entrada invalida")
elif( b != "INTEIRA"):
	print("Entrada invalida")
elif(b != "PLACA"):
	print("Entrada invalida")
elif( d < 1):
	print("Entrada invalida")
elif( d > 8):
	print("Entrada invalida")
elif( b == "INTEIRA" and po < 200):
	print("PO insuficiente")
elif (b == "MALHA" and po <50):
	print("PO insuficiente")
elif( b == "PLACA" and po < 100):
	print("PO insuficiente")
elif(b == "PLACA" and po >= 100):
	print(20*d - 18)
elif(b == "MALHA" and po >= 50):
	print(15*d - 1)
elif(b == "INTEIRA" and po>=200):
	print(30*d -20)		  
		  
		  