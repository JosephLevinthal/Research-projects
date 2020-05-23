a=int(input("valor: "))
b=int(input("quantidade de tickets: "))
c=float(input("valor tickets: "))
d=int(input("quantidade onibus: "))
e=float(input("valor passes: "))
soma= (a - (b * c + d * e))
if(soma >= 0):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")