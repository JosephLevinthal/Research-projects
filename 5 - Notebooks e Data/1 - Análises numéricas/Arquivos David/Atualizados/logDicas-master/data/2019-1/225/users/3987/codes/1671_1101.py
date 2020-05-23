# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("consumo de energia:"))
y = input("tipo: (R/I/C)")

print("Entradas:", x ,"kWh e tipo", y) 
if(x > 0):
	if(y == "R") and (x <= 500):
		z = round(x*0.44,2)
		print("Valor total: R$", z)
	elif(y == "R") and (x > 500):
		w = round(x*0.65,2)
		print("Valor total: R$", w)
	elif(y == "C") and (x <= 1000):
		f = round(x*0.55,2)
		print("Valor total: R$", f)
	elif(y == "C") and (x > 1000):
		g = round(x*0.60,2)
		print("Valor total: R$", g)
	elif(y == "I") and (x <= 5000):
		t = round(x*0.55,2)
		print("Valor total: R$", t)
	elif(y == "I") and ( x > 5000):
		u = round(x*0.60,2)
		print("Valor total: R$", u)
else:
	print("Dados invalidos")

