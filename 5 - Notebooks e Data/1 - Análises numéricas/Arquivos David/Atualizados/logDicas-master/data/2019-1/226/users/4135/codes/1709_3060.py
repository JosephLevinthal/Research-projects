d1= int(input("Digite um numero referente ao valor sorteado no dado 1 (1~6):"))
d2= int(input("Digite um numero referente ao valor sorteado no dado 2 (1~6):"))
r = int (input("Digite um valor referente ao numero de rodadas:"))
if((1<=d1)and(d1<=6)and(1<=d2)and(d2<=6)):
	if(d1+d2==12):
		print("CONSTRICAO")
		print(d1+d2+1)
	elif(d1+d2<5):
		print("POLEN")
		print((d1+d2+1)*r)
	else:
		print("FRAQUEZA")
		print(d1*d2)
else:
	print("Entrada invalida")
