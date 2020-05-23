t = float(input("Insira o valor em graus: "))
v = float(input("Insira a velocidade do vento: "))

if(v > 4.8):
	if(t >= -50 and t <= 10):
		a = (13.12 + (0.6215 * t) - (11.37 * (v ** 0.16)) + (0.3965 * t * (v ** 0.16)))
		print(round(a, 4))
	else:
		print("Temperatura invalida")
else:
	print("Velocidade invalida")