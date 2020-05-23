acai = int(input("Quantidade de acai:"))
salg = int(input("Quantidade de salgados:"))
valor = float(input("Valor pago:"))
quilo = acai/1000
acaipreco = quilo*24
salgado = salg*3
total = acaipreco+salgado
if(valor<=total):
	print(round(total, 2))
	print("Nao")
else:
	print(round(total, 2))
	print("Sim")