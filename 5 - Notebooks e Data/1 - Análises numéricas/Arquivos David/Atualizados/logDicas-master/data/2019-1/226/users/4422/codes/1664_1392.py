consumo = (float(input("Qual o consumo? ")))

if(consumo >= 10):
	cm = (consumo * 3.50) + 30
	print(round(cm, 2))
	
else:
	cm = (consumo * 3.0) + 30
	print(round(cm, 2))