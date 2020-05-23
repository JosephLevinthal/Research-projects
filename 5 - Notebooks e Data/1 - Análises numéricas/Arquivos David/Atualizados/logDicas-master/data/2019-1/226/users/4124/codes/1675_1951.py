x0 = float(input("Coordenada x do ponto p0: "))
y0 = float(input("Coordenada y do ponto p0: "))
x1 = float(input("Coordenada x do ponto p1: "))
y1 = float(input("Coordenada y do ponto p1: "))
x2 = float(input("Coordenada x do ponto p2: "))
y2 = float(input("Coordenada y do ponto p2: "))

c = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if(c < 0):
	print("A direita da reta")
if(c > 0):
	print("A esquerda da reta")
if(c == 0):
	print("Sobre a reta")