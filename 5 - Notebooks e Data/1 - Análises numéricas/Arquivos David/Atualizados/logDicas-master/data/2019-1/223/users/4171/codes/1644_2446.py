senha = int(input("insira uma senha: "))

a1 = senha//100000
a2 = (senha//10000)%10
a3 = (senha//1000)%10
a4 = (senha//100)%10
a5 = (senha//10)%10
a6 = (senha%10)

y = (a2 + a4 + a6) % (a1 + a3 + a5)

if y != 0:
	print("senha invalida")
else:
	print("acesso liberado")