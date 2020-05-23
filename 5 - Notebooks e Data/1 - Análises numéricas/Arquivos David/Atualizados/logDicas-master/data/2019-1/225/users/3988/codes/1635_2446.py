senha = int(input("senha:"))
D1 = (senha // 100000)
D2 = (senha // 10000) % 10
D3 = (senha // 1000) % 10
D4 = (senha // 100) % 10
D5 = (senha // 10) % 10
D6 = (senha % 10)
if ((D2 + D4 + D6) % (D1 + D3 + D5) != 0):
	msg = "senha invalida"
else:
	msg = "acesso liberado"
print(msg)	