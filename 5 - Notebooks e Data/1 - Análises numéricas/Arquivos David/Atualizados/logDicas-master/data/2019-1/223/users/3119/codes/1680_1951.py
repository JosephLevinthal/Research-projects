p0 = float(input("Ponto x0: "))
p_0 = float(input("Ponto y0: "))
p1 = float(input("Ponto x1: "))
p_1 = float(input("Ponto y1: "))
p2 = float(input("Ponto x2: "))
p_2 = float(input("Ponto y2: "))

c = (p1 - p0) * (p_2 - p_0) - (p2 - p0) * (p_1 - p_0)

if(c < 0):
	print("A direita da reta")
elif(c > 0):
	print("A esquerda da reta")
elif(c == 0):
	print("Sobre a reta")	