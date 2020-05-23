x = int(input("Insira o numero: "))
y = int(input("Insira o numero: "))
n = x //10
m = x % 10
k = y // 10
w = y % 10


if((x >= 10) or (x <= 99) or (y >= 10) or (y <= 99)):
	if(x == y):
		print("Ganhou R$ 100.000,00")
	elif((n + m) ==(k + w)):
		print("Ganhou R$ 50.000,00")
	elif((n == k) or (n == w) or (m == k) or (m == w)):
		print("Ganhou R$ 1.000,00")
	else:
		print("Perdeu")
else:
	print("Entrada invalida")