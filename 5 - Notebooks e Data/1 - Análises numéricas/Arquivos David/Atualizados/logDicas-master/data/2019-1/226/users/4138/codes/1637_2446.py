s = int(input(" insira a senha: "))

a = s // 100000
b = s //10000 - (a * 10)
c = s // 1000 - ((a * 100) + (b * 10))
d = s // 100 - ((a * 1000) + (b *100) + (c * 10))
e = s // 10 - ((a * 10000) + (b *1000) + (c * 100) + (d * 10))
f = s % 10

sp = b + d + f
si = a + c + e
if (sp % si != 0):
	mensagem = "senha invalida"
else:
	mensagem = "acesso liberado"

print(mensagem)