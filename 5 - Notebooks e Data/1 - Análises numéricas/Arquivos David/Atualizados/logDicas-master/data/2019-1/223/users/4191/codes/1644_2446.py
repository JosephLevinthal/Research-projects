num=float(input("Digite sua senha de 6 digitod: "))
a= num // 100000
b= (num // 10000) % 10
c=(num // 1000) % 10
d=(num // 100) % 10
e=(num // 10) % 10
f=num % 10
if ((b+d+f)%(a+c+e)== 0):
	mensagem= "acesso liberado"
else:
	mensagem = "senha invalida"
print(mensagem)	