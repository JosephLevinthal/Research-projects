tem = float(input("digite temperatura: "))
vel = float(input("digite velocidade: "))

form = 13.12 + 0.6215 * tem -(11.37 * (vel ** 0.16))+(0.3965 * tem * (vel ** 0.16))

if(tem <= -50 or tem >= 10):
	print("Temperatura invalida")
elif(vel <= 4.8):
	print("Velocidade invalida")
elif(tem > -50 or tem < 10 and vel > 4.8):
	print(round(form, 4))



