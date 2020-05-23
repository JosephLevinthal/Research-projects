h = float(input("horas trabalhadas: "))

h50 = h * 50
x = h-20
h70 = ((h * 50) - (x * 50)) +(x) *70
if (h > 20):
	print(round(h70,2))
else:
	print(round(h50,2))
	