h = float(input("Quantidade de horas: "))

if(h > 20):
	p = (20*50 + ((h-20)*70))
	print(round(p,2))
else:
	p = (h*50)
	print(round(p,2))