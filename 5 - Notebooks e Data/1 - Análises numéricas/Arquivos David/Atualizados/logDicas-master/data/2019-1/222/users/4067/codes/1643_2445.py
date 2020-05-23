escala = input("")
valor = float(input(""))
if escala.upper() == "F":
	mensagem = 5/9*(valor - 32)
else:
	mensagem = (9/5*valor) + 32
print(round(mensagem,2))
	