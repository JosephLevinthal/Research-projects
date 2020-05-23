nj = int(input("Numero apostado: "))
nl = int(input("Numero da loteria: "))

a1 = nj // 10
b1 = nj % 10
a2 = nl // 10
b2 = nl % 10

if(nj == nl):
	print("Ganhou R$ 100.000,00")
elif(a1 == b2 and a2 == b1):
	print("Ganhou R$ 50.000,00")
elif(a1 == a2 or b1 == b2 or a1 == b2 or a2 == b1):
	print("Ganhou R$ 1.000,00")
else: 
	print("Perdeu")
	