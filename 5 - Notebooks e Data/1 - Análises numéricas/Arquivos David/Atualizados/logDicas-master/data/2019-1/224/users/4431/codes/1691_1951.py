x0=float(input("Digite o x0: "))
y0=float(input("Digite o y0: "))
x1=float(input("Digite o x1: "))
y1=float(input("Digite o y1: "))
x2=float(input("Digite o x2: "))
y2=float(input("Digite o y2: "))
c=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
if(c<0):
	print("A direita da reta")
elif(c>0):
	print("A esquerda da reta")
else:
	print("Sobre a reta")