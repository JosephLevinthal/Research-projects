consumo= float(input("digite o consumo: "))
tipo=input("tipo instalacao: ")
tipo=tipo.upper()
if (tipo=="R" and 0 <= consumo <= 500):
	preco= consumo * 0.44
	print("Entradas:", consumo,"kWh  e tipo", tipo)
	print("Valor total: R$", preco)
elif( tipo=="R" and consumo> 500):
	preco= consumo * 0.65
	print("Entradas:", consumo,"kWh  e tipo", tipo)
	print("Valor total: R$", preco)
elif( tipo=="C" and 0<=consumo<= 1000):
	preco= consumo * 0.55
	print("Entradas:", consumo,"kWh  e tipo", tipo)
	print("Valor total: R$", preco)
elif( tipo=="C" and consumo> 1000):
	preco= consumo * 0.60
	print("Entradas:", consumo,"kWh  e tipo", tipo)
	print("Valor total: R$", preco)
elif( tipo=="I" and 0<=consumo<= 5000):
	preco= consumo * 0.55
	print("Entradas:", consumo,"KWh e tipo", tipo)
	print("Valor total: R$", preco)
elif( tipo=="I" and consumo> 5000):
	preco= consumo * 0.60
	print("Entradas:", consumo,"kWh  e tipo", tipo)
	print("Valor total: R$", preco)
else:
	print("Entradas:", consumo, "kWh   e tipo", tipo)
	print("Dados invalidos")