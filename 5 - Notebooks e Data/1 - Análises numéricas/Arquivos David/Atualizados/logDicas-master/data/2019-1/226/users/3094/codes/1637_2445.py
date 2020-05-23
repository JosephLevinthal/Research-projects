escala = input("C ou F: ").upper()
temp = float(input("temperatura: "))
if(escala == "F"):
	x = 5/9 * (temp - 32)
	print(x)
else:
	y = ((9 * temp) / 5) + 32
	print(y)