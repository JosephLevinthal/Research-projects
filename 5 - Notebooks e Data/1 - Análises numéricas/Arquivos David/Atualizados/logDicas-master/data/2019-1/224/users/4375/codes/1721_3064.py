cab=input("nome da cabeca AAMEUL, HETHRADIAH ou RAKSHASA: ")
valor=int(input("valor dos dados: "))
valor2=int(input("valor dos dados: "))
cab=cab.upper()
if(valor<10)and(valor2<10)and(cab=="AAMEUL"):
	msg=valor+valor2+8
	print(msg)
elif(valor<10) and (valor2<10) and(cab=="HETHRADIAH"):
	msg=(valor+valor2)*2
	print(msg)
elif(valor<10)and(valor2<10)and(cab=="RAKSHASA"):
	msg=valor+valor2+10
	print(msg)
else:
	print("Entrada invalida")
	
	print()
