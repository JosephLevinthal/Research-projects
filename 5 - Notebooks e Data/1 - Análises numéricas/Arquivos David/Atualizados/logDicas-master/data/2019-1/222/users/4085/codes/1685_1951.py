x0 = float(input("escreva a abscissa de p0: "))
y0 = float(input("escreva a ordenada de p0: "))
x1 = float(input("escreva a abscissa de p1: "))
y1 = float(input("escreva a ordenada de p1: "))
x2 = float(input("escreva a abscissa de p2: "))
y2 = float(input("escreva a ordenada de p2: "))
c = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
if (c > 0):
	print ("A esquerda da reta")
elif (c < 0):
	print ("A direita da reta")
else:
	print ("Sobre a reta")