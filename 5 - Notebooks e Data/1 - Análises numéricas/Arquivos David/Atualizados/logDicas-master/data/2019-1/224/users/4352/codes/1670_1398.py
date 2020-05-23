tempo = float(input("digite o tempo de voo, em minutos: "))
custo1 = 5000 + tempo*100
custo2 = 8000 + 20000 + (tempo-200)*90
if tempo <= 200:
	print(round(custo1, 2))
else: 
	print(round(custo2, 2))