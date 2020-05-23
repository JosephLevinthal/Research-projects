t = float(input("tmperatura do ar: "))
v = float(input("velocidade do vento: "))
if (t < -50 or t > 10):
	print("Temperatura invalida")

elif (v <= 4.8):
	print("Velocidade invalida")
	
else:
	o = 13.12 + 0.6215 * t - (11.37 * v**0.16) + (0.3965 * t * v**0.16)
	print(round(o, 4))