po=int(input("quantidades de pecas de ouro: "))
y=input("nome da armadura escolhida: ").upper() #lower
d= int(input("fator de destreza: "))

if(y == "INTEIRA") and (po>=200):
	r=(30*d-20)
	print(r)
elif(y=="MALHA") and (po>=50):
	r=(15*d-1)
	print(r)
elif(y=="PLACA") and (po>=100):
	r=(20*d-18)
	print(r)
else: 
	r=("PO insuficiente")
	print(r)
