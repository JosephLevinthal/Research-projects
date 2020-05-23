num = int(input("insira a senha de 1 a 5 digitos:"))
d1 = num // 100000 % 10
d2 = num // 10000 % 10
d3 = num // 1000 % 10
d4 = num // 100 % 10
d5 = num // 10 % 10
d6 = num %10
if ((d2 + d4 + d6) % (d1 + d3 + d5) != 0): 
	print("senha invalida")
else:
	print("acesso liberado")