# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
con = float(input())
t   = input()

def prt (x):
	print("Entradas: ",con," kWh e tipo ",t)
	print("Valor total: R$ ",round(x,2))

if t == "R" and con>0:
	x = con*.44 if con<=500 else con*.65
	prt (x)
elif t == "C" and con>0:
	x = con*.55 if con<=1000 else con*.60
	prt (x)
elif t == "I" and con>0:
	x = con*.55 if con<=5000 else con*.60
	prt()
else:
	print("Entradas: ",con," kWh e tipo ",t)
	print("Dados invalidos")

