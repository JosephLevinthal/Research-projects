senha = int(input("Qual sua senha: "))

x1 = senha // 1 % 10
x2 = senha // 10 % 10
x3 = senha // 100 % 10
x4 = senha // 1000 % 10
x5 = senha // 10000 % 10
x6 = senha // 100000 % 10

c = (x1 + x3 + x5) % (x2 + x4 + x6)
v = (x2 + x4 + x6) % (x1 + x3 + x5)

if (c == 0) or (v == 0):
	mensagem = "acesso liberado"
else:
	mensagem = "senha invalida"
	
print(mensagem)