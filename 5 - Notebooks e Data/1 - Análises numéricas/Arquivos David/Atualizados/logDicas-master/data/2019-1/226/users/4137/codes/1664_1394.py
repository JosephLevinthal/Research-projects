h = int(input("Quantidade de horas trabalhadas:"))

if(h<=20):
	x = h*50
	
else:	
	x = (50*20) + ((h-20)*70)
	
print(float(round(x, 2)))