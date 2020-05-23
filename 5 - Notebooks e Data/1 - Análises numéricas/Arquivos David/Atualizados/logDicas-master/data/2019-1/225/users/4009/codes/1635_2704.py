nota = float(input("nota: "))
bonificacao = input("S/N")
acrescimo = nota*0.10
notafinal = nota+acrescimo

if bonificacao == "S":
	print(notafinal)
else:
	print(nota)