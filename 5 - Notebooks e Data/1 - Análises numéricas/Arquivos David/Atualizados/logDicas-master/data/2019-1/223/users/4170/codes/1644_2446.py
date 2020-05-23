senha = int(input("Senha: "))
a = (senha//100000)
b = (senha//10000)%10
c = (senha//1000)%10
d = (senha//100)%10
e = (senha//10)%10
f = (senha)%10
calculo = (b+d+f)%(a+c+e)
if(calculo ==0):
	mensagem = "acesso liberado"
	print(mensagem)
else:
	mensagem = "senha invalida"
	print(mensagem)