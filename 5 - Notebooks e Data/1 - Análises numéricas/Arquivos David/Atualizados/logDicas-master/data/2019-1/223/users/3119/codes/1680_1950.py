temp = float(input("Temperatura em Celsius: "))
vento = float(input("Velocidade do vento em km/h: "))

if((temp >= -50 and temp <= 10)):
	if(vento > 4.8):
		theta = 13.12 + 0.6215 * temp - (11.37 * vento ** 0.16) + (0.3965 * temp * vento ** 0.16)
		print(round(theta,4))
	else:
		print("Velocidade invalida")
else:
	print("Temperatura invalida")

