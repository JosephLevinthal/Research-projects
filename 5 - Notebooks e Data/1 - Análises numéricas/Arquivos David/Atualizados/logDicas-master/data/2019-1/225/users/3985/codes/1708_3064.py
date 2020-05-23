x= input("Nome da cabeca: (AAMEUL/HETHRADIAH/RAKSHASA)?")
d1= int(input("Valor do dado:"))
d2= int(input("Valor do dado:"))

if(x=="AAMEUL")or(x=="HETHRADIAH")or(x=="RAKSHASA")or((d1>1)and(d1<10))or((d2>1)and(d2<10)):
	if (x=="AAMEUL"):
		dano= (d1+d2)+8
		print(dano)
	elif (x=="HETHRADIAH"):
		dano= 2*(d1+d2)
		print(dano)
	elif (x=="RAKSHASA"):
		dano= (d1+d1)+10
		print(dano)
else:
		print("Entrada invalida")

	
	
	
	
	