sen = int(input("Digite a senha: "))
n1 = sen//100000
n2 = (sen//10000)%10
n3 = (sen//1000)%10
n4 = (sen//100)%10
n5 = (sen//10)%10
n6 = sen%10

if((n2 + n4 + n6)%(n1 + n3 + n5) != 0):
	print("senha invalida")
else:
	print("acesso liberado")
