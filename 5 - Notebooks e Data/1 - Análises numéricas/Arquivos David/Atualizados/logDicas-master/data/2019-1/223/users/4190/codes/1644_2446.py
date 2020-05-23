senha = int(input('Insira a senha de ate seis digitos: '))

num1 = senha // 1 % 10
num2 = senha // 10 % 10
num3 = senha // 100 % 10
num4 = senha // 1000 % 10
num5 = senha // 10000 % 10
num6 = senha // 100000 % 10

soma1 = num5+num3+num1
soma2 = num6+num4+num2

if (soma1%soma2==0):
	mensagem = 'Acesso liberado'
	
else:
	mensagem = 'Senha invalida'
	
print(mensagem.lower())