T = float(input())
v = float(input())

if(T < -50 or T > 10):
	print("Temperatura invalida")
elif(v <= 4.8):
	print("Velocidade invalida")
else:
	sf = 13.12 + 0.6215 * T - (11.37 * v ** 0.16) + (0.3965 * T * v ** 0.16)
	print(round(sf, 4))