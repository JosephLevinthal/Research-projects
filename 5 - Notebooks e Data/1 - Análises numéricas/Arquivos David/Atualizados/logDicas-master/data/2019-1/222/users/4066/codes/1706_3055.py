valor = float(input("Valor consumido: "))

if (valor <= 100):
	g = valor*0.1
elif (valor > 100 and valor <= 200):
	g = valor*0.09
elif (valor > 200 and valor <=300):
	g = valor*0.08
elif (valor > 300):
	g = valor*0.07
	
vt = valor + g

print(round(vt,2))