from math import*
x = (float(input("valor de x: ")))
if(x>=-4 and x<0):
	y = round(abs(x)**0.5, 4)
elif(x==0):
	y = 0
elif(x>0 and x<=4):
	y = round(x**0.5, 4)
else:
	y = "entrada invalida"
print(y)