T = float(input("insira a temperatura:"))
v = float(input("insira a velocidade do vento:"))

A = 13.12 + (0.6215 * T) -(11.37 * (v ** 0.16)) +(0.3965 * T * (v ** 0.16))

if(v > 4.8):
	if(T >= -50 and  T <= 10):
		print(round(A,4))
	elif(T < -50 or T > 10):
		print("Temperatura invalida")
else:
	print("Velocidade invalida")
	