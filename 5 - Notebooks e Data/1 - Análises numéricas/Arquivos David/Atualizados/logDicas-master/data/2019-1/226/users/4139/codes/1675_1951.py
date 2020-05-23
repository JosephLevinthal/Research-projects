px0 = float(input("x0 de p0:"))
py0 = float(input("y0 de p0:"))
px1 = float(input("x1 de p1:"))
py1 = float(input("y1 de p1:"))
px2 = float(input("x2 de p2:"))
py2 = float(input("y2 de p3:"))

c=(px1-px0)*(py2-py0)-(px2-px0)*(py1-py0)

if(c<0):
	print("A direita da reta")
elif(c>0):
	print("A esquerda da reta")
elif(c==0):
	print("Sobre a reta")
