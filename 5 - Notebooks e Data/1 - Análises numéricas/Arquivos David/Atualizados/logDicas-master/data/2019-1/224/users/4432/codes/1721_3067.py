a=input("ataque espada ou cauda   ")
b=int(input("numero  "))
c=int(input("nu   "))
d=int(input("dfsdfg "))
e=int(input("fdfgd  "))
if(a=="CAUDA")or(a=="ESPADA"):
	if(b<=0)or(b>=7)or(c<=0)or(c>=7)or(d<=0)or(d>=7)or(e<=0)or(e>=7):
		print("Entrada invalida")
	elif(a=="CAUDA"):
		z=(b+c+d)*e
		print(z)
	elif(a=="ESPADA"):
		z=(b+6)+(c+6)+(d+6)+(e+6)
		print(z)
else:
	print("Entrada invalida")
	
	