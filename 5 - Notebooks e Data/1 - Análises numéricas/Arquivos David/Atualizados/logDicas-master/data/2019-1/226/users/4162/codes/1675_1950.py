tc= float(input("insira a temperatura do ar em graus celsius: "))
v= float(input("insira a velocida do vento em Km/h: "))
ro= 13.12+(0.6215*tc)-(11.37*(v**0.16))+(0.3965*tc*(v**0.16))
if (tc<-50)or(tc>10):
	print("Temperatura invalida")
if v<=4.8:
	print("Velocidade invalida")
if (tc>= -50)and(tc<=10)and(v>4.8):
	print(round(ro,4))
