x = int(input("numero de dois digitos:"))
y = int(input("numero sorteado na loteria:"))

x1 = x - (x //10)*10
x2 = x //10

y1 = y - (y //10)*10
y2 = y //10

if(x == y):
	print("Ganhou R$ 100.000,00")
elif(x1 == y1) or (x1 == y2) or (x2 == y1) or (x2 == y2):
	print("Ganhou R$ 1.000,00")
elif(x1 == y2) and (x2 == y1):
	print("Ganhou R$ 50.000,00")
else:
	print("Perdeu")
	
