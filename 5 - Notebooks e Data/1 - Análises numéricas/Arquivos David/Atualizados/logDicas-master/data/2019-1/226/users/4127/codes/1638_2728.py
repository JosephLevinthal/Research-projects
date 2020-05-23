km= float(input("quantos km?"))
car= input("qual o tipo de carro?")
if(car.upper()=="A"):
	print(round(km/8,2))
if(car.upper()=="B"):
	print(round(km/12,2))