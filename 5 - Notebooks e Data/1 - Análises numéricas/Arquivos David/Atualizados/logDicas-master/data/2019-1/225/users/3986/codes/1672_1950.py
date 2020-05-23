t=float(input("temperatura em C:"))
v=float(input("velocidade em km/h:"))
x= 13.12 + 0.6215*t - (11.37*(v**0.16)) + (0.3965*t*(v**0.16))
if t<=10 and t>=-50 and v>4.8 :
	print(round(x,4))
elif t<=10 and t>=-50 and v<=4.8:
	print("velocidade invalida")
else:
	print("Temperatura invalida")