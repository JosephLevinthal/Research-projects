from math import*
x=float(input("Insira o valor de X:"))
xab=abs(x)**0.5
X=x**0.5
if(-4<=x or x<0):
	print(round(xab,4))
elif(x==0):
	print(0)

elif(0<x or x>=4):
	print(round(X,4))
else:
	print("entrada invalida")