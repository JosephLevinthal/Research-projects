d1=int(input("Entre com o valor do dado lancado d1: "))
d2=int(input("Entre com o valor do dado lancado d2: "))
r=int(input("Digite o numero de rodadas?: "))

print(d1)
print(d2)
print(r)

d=d1+d2
CONTRICAO=d1+d2+1
POLEN=(d1+d2+1)*r
FRAQUEZA=d1*d2

if d1<1 and d1>6 and d2<1 and d2>6 and r<0:
	print ("Entrada invalida")

elif d==12:
	print("CONSTRICAO")
	print(CONTRICAO)
	
elif d<=5:
	print("POLEN")
	print(POLEN)
	
elif d>5 and d==11:
	print("FRAQUEZA")
	print(FRAQUEZA)
else:
	print("Entrada invalida")
	

	