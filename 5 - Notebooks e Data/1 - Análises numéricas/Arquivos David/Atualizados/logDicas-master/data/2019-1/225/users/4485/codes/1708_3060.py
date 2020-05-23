d1=int(input("valor sorteado?"))
d2=int(input("valor sorteado?"))
r= int(input("numero de rodadas?"))
if(d1+d2==12):
	print("CONSTRICAO")
	print(d1+d2+1)
elif(d1+d2>5):
	print("POLEN")
	print((d1+d2+1)*r)
elif(r>6):
	print("Entrada invalida")
else:
	prin