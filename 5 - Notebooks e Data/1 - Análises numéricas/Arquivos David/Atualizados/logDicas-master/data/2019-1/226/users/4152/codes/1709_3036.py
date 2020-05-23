x = float(input("Digite aqui o valor de x: "))
if ((x <= -1) or (x >= 1)):
	x = x
elif (((x > -1) and (x < 0)) or ((x > 0) and (x < 1))):
	x = 1
else:
	x = 2
print(round(x, 2))