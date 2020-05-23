t=float(input("temperatura:"))
v=float(input("velocidade:"))

o=13.12+(0.6215*t)-(11.37*(v**0.16))+(0.3965*t*(v**0.16))
if((t>=-50 and t<10)and(v>=4.8)):
	print(round(o, 4))
elif(v<4.8):
	print("Velocidade invalida")
else:
	print("Temperatura invalida")