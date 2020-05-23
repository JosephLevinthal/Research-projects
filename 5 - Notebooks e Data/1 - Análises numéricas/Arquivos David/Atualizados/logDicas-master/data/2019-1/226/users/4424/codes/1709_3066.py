vida=int(input("valor: "))
x=float(input("valor: "))
y=float(input("valor: "))
z=float(input("valor: "))

N=x+y+z
q=(vida-(10*N))
if(N>=3)and(N<=36):
	if(q>0):
		print(q)
		print("VIVO")
	elif(q<=0):
		print(0)
		print("MORTO")		
else:
	print("Entrada invalida")