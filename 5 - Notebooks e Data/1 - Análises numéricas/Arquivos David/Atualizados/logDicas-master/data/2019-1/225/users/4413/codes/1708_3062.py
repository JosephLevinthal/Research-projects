a=float(input("pecas de ouro: "))
b=input("arma: ")
c=int(input("fator de sucesso: "))
if(c<1)or(c>10):
	print("Entrada invalida")
elif(a>=100)and(b=="ESPADA"):
	print(c*10)
	
elif(a>=50)and(b=="MARRETA"):
	print(c+5)
	
elif(a>=30)and(b=="MACHADO"):
	print(c+3)
	
else:
	print("PO insuficiente")