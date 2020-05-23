s = int(input("Senha: "))
d1 = s//100000
d2 = (s//10000)%10
d3 = (s//1000)%10
d4 = (s//100)%10
d5 = (s//10)%10
d6 = s%10

if ((d2 + d4 + d6) % (d1 + d3 + d5) != 0):
	print("senha invalida")
else:
	print("acesso liberado")