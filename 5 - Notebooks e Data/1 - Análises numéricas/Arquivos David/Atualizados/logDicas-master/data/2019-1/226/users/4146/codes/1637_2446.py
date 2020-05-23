senha = float(input("Digite a senha: "))

a = senha//100000
b = (senha//10000)%10
c = (senha//1000)%10
d = (senha//100)%10
e = (senha//10)%10
f = senha%10

if ((b+d+f)%(a+c+e) == 0):
	mensagem = "acesso liberado"
else:
	mensagem = "senha invalida"
	
print(mensagem)	