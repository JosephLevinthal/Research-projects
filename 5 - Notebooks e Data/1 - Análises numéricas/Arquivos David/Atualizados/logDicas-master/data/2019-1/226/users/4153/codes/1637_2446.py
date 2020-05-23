s = int(input("Insira sua senha: "))

x = s // 100000
x2 = (s // 10000) - (x * 10)
x3 = (s // 1000) - (s // 10000)*10
x4 = (s // 100) - (s // 1000)*10
x5 = (s // 10) - (s // 100)*10
x6 = (s % 10)

operacao = x2 + x4 + x6
op2 = x + x3 + x5
mult = operacao % op2
if(mult == 0):
	msg = "acesso liberado"
else:
	msg = "senha invalida"
print(msg)