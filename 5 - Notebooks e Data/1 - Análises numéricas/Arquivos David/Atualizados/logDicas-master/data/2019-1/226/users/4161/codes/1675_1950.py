t = float(input("temperatura do ar: "))
v = float(input("velocidade do vento: "))

if not(-50<=t<=10): 
	print("Temperatura invalida")
elif not(v>4.8):
	print("Velocidade invalida")
else:
	teta = 13.12 +0.6215*t - (11.37*(v**0.16))+(0.3965*t*(v**0.16))
	print(round(teta, 4))