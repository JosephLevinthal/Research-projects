a = int (input("Qual o numero apostodado pelo jogador: "))
b = int(input("Numero sorteador: "))

c = a // 10
c1 =  a % 10
d = b // 10
d1 = b % 10
if a == b :
	print("Ganhou R$ 100.000,00")
elif ((c == d) and (c1 == d1)) or ((c == d1) and (d == c1)):
	print("Ganhou R$ 50.000,00")
elif ((c== d)or (c == d1) or (d == c1) or (d1 == c1)):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")
