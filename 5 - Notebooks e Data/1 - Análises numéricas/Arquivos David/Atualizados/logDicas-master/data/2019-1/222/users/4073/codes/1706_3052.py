a=float(input("Qual o consumo?"))
if (a>= 0 and a<= 10):
	valor=(a*3)+15
	print(round(valor,2))
elif (a>= 10 and a<= 15):
	valor=(a*3.5)+20
	print(round(valor,2))
elif (a>= 15 and a<= 20):
	valor=(a*4)+25
	print(round(valor,2))
else:
	valor=(a*4.5)+30
	print(round(valor,2))