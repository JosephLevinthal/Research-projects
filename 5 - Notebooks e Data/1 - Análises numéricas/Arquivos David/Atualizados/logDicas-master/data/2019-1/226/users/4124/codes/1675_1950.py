temp = float(input("Temperatura em celsius: "))
vel = float(input("Velocidade do vento: "))

if(temp < -50 or temp > 10):
	print("Temperatura invalida")
elif(vel < 4.8):
	print("Velocidade invalida")
else:
	s = 13.12 + 0.6215 * temp - (11.37 * vel ** 0.16) + (0.3965 * temp * vel ** 0.16)
	print(round(s, 4))