q = float(input("quantidade de horas: "))

if q<=20:
	print(round(50*q, 2))
	
else:
	print(round((50*20)+((q-20)*70), 2))