escala = input("Escala em que a temperatura está representada: C para Celsius, ou F para Fahrenheit ")
valor = float(input("Qual o valor da temperatura? "))
if (escala.upper() == "F") :
	C = (valor - 32)*(5/9)
	print(round(C, 2))
else :
	F = (valor*1.8)+32
	print(round(F, 2))