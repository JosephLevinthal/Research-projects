num = int(input("Digite a senha (6 digitos): "))

d1 = (num // 100000)
d2 = (num // 10000) % 10
d3 = (num // 1000) % 10
d4 = (num // 100) %10
d5 = (num // 10) %10
d6 = (num // 1) %10

if((d2 + d4 +d6) // (d1 + d3 + d5) == 2  ):
	print("acesso liberado")
else:
	print("senha invalida")
	
