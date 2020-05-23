a = int(input( "digite a sua senha: "))

b = a//100000 #1
c = a%100000 #23456

d = c // 10000 # 2
e = c % 10000 # 3456

f = e // 1000 #3
g = e % 1000 #456

h =  g // 100 # 4
i = g % 100 # 56

j = i // 10 # 5
k = i % 10 # 6

soma = d + h + k
multiplo = b + f + j

if (soma % multiplo == 0 ):
	mensagem = "acesso liberado"
else: 
	mensagem = "senha invalida"

print(mensagem)