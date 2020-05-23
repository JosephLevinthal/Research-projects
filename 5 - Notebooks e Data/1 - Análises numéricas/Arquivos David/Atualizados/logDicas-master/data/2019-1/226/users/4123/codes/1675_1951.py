x0 = float(input())
y0 = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

c = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
if c<0:
	print("A direita da reta")
elif c>0:
	print("A esquerda da reta")
else:
	print("Sobre a reta")