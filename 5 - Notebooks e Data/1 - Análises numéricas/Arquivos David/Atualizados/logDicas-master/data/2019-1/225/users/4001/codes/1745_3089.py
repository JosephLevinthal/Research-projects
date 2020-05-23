n = int(input("Movimento: "))
soma = 0 #acumuladora
while (n < 0 or n > 0):
	soma = soma + n
	n = int(input("Movimento: "))
print(soma)
if (soma < 0):
	print("Esquerda")
elif (soma > 0):
	print("Direita")
else:
	print("Inicial")
