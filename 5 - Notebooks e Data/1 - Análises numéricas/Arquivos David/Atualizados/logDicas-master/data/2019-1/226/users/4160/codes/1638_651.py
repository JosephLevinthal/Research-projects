h = float(input("Digite a altura (em metros): "))
s = input("Digite o sexo (M ou F): ").upper()

if(s == "M"):
	x = (72.7 * h) - 58
	print(round(x,2))
else: 
	y = (62.1 * h) - 44.7
	print(round(y,2))