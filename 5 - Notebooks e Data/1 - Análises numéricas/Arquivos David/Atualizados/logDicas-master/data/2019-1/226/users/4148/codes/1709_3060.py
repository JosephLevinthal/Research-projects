d1 = int(input("dado 1: "))
d2 = int(input("dado 2: "))
r = int(input("numero de rodadas: "))	

c = d1 + d2 +1
p = (d1+d2+1)*r
f = (d1*d2)

if(d1<=6 and d2<=6):
	if(d1+d2==12):
		print("CONSTRICAO")
		print(c)
	elif((d2+d1)<5):
		print("POLEN")
		print(p)
	else:
		print("FRAQUEZA")
		print(f)
else:
	print("Entrada invalida")