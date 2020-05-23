p1= int(input("insira o x0: "))
p2= int(input("insira o y0: "))
p3= int(input("insira o x1: "))
p4= int(input("insira o y1: "))
p5= int(input("insira o x2: "))
p6= int(input("insira o y2: "))
c=(p3-p1)*(p6-p2)-(p5-p1)*(p4-p2)
if c<0:
	print("A direita da reta")
elif c>0:
	print("A esquerda da reta")
elif c==0:
	print("Sobre a reta")