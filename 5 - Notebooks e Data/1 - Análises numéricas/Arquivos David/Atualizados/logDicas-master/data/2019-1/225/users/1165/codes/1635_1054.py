x = float(input("Leia o x de um plano cartesiano: "))
y = float(input("Leia o y de um plano cartesiano: "))

if (2 * x + y == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"

print(mensagem.lower())
