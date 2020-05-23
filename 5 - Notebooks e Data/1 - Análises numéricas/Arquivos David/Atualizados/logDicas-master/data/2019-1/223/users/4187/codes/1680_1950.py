Temp = float(input("digite a temperatura(entre -50C e 10C):"))
velVento = float(input("digite a velocidade (acima de 4,8KM/h):"))

#alfa é a sensacao de frio
alfa = ((13.12) + (0.6215 * Temp) - ((11.37) * (velVento**0.16)) + ((0.3965 *  Temp) * (velVento**0.16)))

if(Temp < -50 or Temp > 10):
	print("Temperatura invalida")
elif(velVento < 4.8):
	print("Velocidade invalida")
else:
	print(round(alfa,4))