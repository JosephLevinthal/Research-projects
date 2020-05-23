x0 = float(input("insira a coordenada x0:"))
y0 = float(input("insira a coordenada y0:"))
x1 = float(input("insira a coordenada x1:"))
y1 = float(input("insira a coordenada y1:"))
x2 = float(input("insira a coordenada x2:"))
y2 = float(input("insira a coordenada y2:"))

c = (x1 - x0) * (y2 - y0) - ((x2 - x0) *(y1 - y0))
 
if(c < 0):
	print("A direita da reta")
elif(c > 0):
	print("A esquerda da reta")
elif(c == 0):
	print("Sobre a reta")

