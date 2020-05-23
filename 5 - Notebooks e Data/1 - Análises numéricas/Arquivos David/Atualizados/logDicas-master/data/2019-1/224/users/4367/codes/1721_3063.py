a=int(input("diga a quantidade de ouros: "))
b=input("escolha o tipo de armadura MALHA, PLACA ou INTEIRA: ")
c=int(input("escolha um valor entre 1 e 8: "))

if (b=="inteira".upper()) and (a>=200):
	f= 30*c-20
	print(f)

elif (b=="malha".upper()) and (a>=50):
	f=15*c-1
	print(f)
elif(b=="placa".upper()) and (a>=100):
	f=20*c-18
	print(f)
else:
	print("PO insuficiente")