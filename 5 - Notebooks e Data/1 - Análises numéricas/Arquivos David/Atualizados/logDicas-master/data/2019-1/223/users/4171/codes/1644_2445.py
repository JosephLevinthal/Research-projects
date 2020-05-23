escala = input("Celsius/Fahrenheit (C/F): ")
temp = float(input("Temperatura atual: "))

if escala == "F":
	t = (5 / 9) * (temp - 32)
	print(round(t,4))
else:
	t = (9*temp)/5 + 32
	print(round(t,4))

