# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("escreva a abscissa do ponto: "))
y = float(input("escreva a ordenada do ponto: "))
if (y < 0):
	mensagem = "Inferiores"
else:
	mensagem = "Superiores"
print(mensagem)