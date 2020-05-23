s = int(input("Digite uma senha de 6 digitos : "))
#soma dos digitos da SEGUNDA, QUARTA E SEXTA POSIÇÃO
a = s // 100000
b = (s % 100000) // 10000
c = (s % 100000) % 10000 // 1000
d = (s % 100000) % 1000 // 100
e = (s % 100000) % 100 // 10
f = (s % 100000) % 100 % 10
if((b + d + f) % (a + c + e) == 0):
	mensagem = "acesso liberado"
	print(mensagem)
else:
	mensagem = "senha invalida"
	print(mensagem)
#Soma dos 6 digitos inseridos pelo usuário  print(a + b + c + d + e + f)

