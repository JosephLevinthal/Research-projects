num = int(input("Digite aqui a sua senha de : "))

n1 = num // 100000
n2 = (num // 10000) % 10
n3 = (num // 1000) % 10
n4 = (num // 100) % 10
n5 = (num // 10) % 10
n6 = num % 10

total = (n2 + n4 + n6) // (n1 + n3 + n5)

if (total == 2):
	msg = "acesso liberado"
else:
	msg = "senha invalida"
	
print(msg)