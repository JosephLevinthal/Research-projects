senha = int(input("Informe a senha: "))

num1 = senha // 100000
num2 = senha // 10000 % 10
num3 = senha // 1000 % 10
num4 = senha // 100 % 10
num5 = senha // 10 % 10
num6 = senha % 10

soma1 = num2 + num4 + num6
soma2 = num1 + num3 + num5

if ((soma1 % soma2) == 0):
	print ("acesso liberado")
else:
	print ("senha invalida")
