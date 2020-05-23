# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("escreva o numero de horas extras: "))
f = float(input("escreva o numero de horas que faltou: "))
h = (e - (1/4 * f))
print (e, "extras e", f, "de falta")
if (h <= 400):
	mensagem = 100.00
	print ("R$", round(mensagem, 2))
else:
	mensagem = 500.00
	print ("R$", round(mensagem, 2))