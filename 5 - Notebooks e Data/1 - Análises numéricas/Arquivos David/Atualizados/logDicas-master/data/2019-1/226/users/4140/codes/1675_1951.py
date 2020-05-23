x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())

c=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
if(c<0):
	print("A direita da reta")
elif(c>0):
	print("A esquerda da reta")
else:
	print("Sobre a reta")