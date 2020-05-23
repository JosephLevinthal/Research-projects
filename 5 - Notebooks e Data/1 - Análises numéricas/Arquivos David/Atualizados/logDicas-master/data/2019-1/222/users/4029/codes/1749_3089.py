n = int(input("Digite um numero: "))
s = 0
while ( n != 0):
	s = s + n
	n = n + 1
	if (n > 1):
		msg = "Direita"
	else:
		msg = "Esquerda"
else:
	n = int(input("Digite um numero: "))
	print(n)
	print(msg)

		

		