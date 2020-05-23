a = int(input("escreva o valor do coeficiente a: "))
b = int(input("escreva o valor do coeficiente b: "))
c = int(input("escreva o valor do coeficiente c: "))
d = int(input("escreva o valor do coeficiente d: "))
e = int(input("escreva o valor do coeficiente e: "))
f = int(input("escreva o valor do coeficiente f: "))
x = (c * e) - (b * f)/(a * e) - (b * d)
y = (a * f) - (c * d)/ (a * e) - (b * d)
if ((a * e) - (b * d) == 0):
	mensagem = "Nao tem solucao"
else:
	mensagem = x, y

print(mensagem)