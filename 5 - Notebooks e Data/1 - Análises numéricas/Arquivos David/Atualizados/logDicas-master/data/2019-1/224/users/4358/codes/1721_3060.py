d1=int(input("Digite de 1 a 6:"))
d2=int(input("Digite de 1 a 6:"))
r=int(input("Digite o numero de rodadas:"))
p1=d1+d2+1
p2=(d1+d2+1)*r
p3=d1*d2
if((d1<1)or(d1>6)or((d2<1))or(d2>6)):
	print("Entrada invalida")
elif(d1+d2==12):
	print("CONSTRICAO")
	print(p1)
elif(d1+d2<5):
	print("POLEN")
	print(p2)
else:
	print("FRAQUEZA")
	print(p3)
