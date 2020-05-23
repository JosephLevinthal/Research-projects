num = int(input("senha:"))

# decompoe os 6 digitos da senha
d1 = num // 100000
d2 = (num % 100000) // 10000
d3 = (num % 10000) // 1000
d4 = (num % 1000) // 100
d5 = (num % 100) // 10
d6 = num % 10
if((d2 + d4 + d6) % (d1+ d3 + d5) != 0):
	msg = "senha invalida"
else:
	msg = "acesso liberado"
print(msg)