x0 = float(input("coordenada: "))
y0 = float(input("coordenada: "))
x1 = float(input("coordenada: "))
y1 = float(input("coordenada: "))
x2 = float(input("coordenada: "))
y2 = float(input("coordenada: "))

c = (x1 - x0)*(y2 - y0) - (x2 - x0) * (y1 - y0)

if c < 0 :
	print("A direita da reta")
elif c > 0:
	print("A esquerda da reta")
elif c == 0 : 
	print("Sobre a reta")