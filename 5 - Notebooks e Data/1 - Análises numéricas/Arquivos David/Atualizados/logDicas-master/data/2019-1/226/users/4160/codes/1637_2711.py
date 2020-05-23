dinheiro = float(input("Digite quanto voce possui: "))
qnt = int(input("Digite a quantiade de tickets que voce precisa: ")) 
vt = float(input("Digite o valor do ticket do ru: "))
passes = int(input("Digite a quantidade de passes de onibus: "))
vp = float(input("Digite o valor dos passes de onibus: "))

if (dinheiro < (qnt * vt) + (passes * vp)):
	print("INSUFICIENTE")
else:
	print("SUFICIENTE")
