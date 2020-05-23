# Entradas
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

if ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) < 0):
	print("A direita da reta")
elif ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0):
	print("Sobre a reta")
else:
	print("A esquerda da reta")