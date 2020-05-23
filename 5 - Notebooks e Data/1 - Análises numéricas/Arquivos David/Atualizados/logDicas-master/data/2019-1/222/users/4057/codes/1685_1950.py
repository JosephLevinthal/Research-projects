c = float(input("Qual a temperatura em celsius: "))
v = float(input("Qual a velocidade em km/h: "))

a = (0.3965 * c * v**0.16)
b = (11.37 * v**0.16)
m = 0.6215
n = 13.12
if ((c >= (-50))and(c <= 10)):
	if (v > 4.8):
		O = (n + m * c - b + a )
		print(round(O, 4))
	else: 
		print("Velocidade invalida")
else:
	print("Temperatura invalida")
