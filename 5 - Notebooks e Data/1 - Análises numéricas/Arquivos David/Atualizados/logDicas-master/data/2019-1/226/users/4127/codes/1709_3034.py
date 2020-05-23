from math import*
x= float(input("qual seu numero x? "))

if(x<-4 or x>4):
	print("entrada invalida")
elif(-4<=x<0):
	print(round(sqrt(abs(x)),4))
elif(x==0):
	print(0)
elif(0<x<=4):
	print(round(sqrt(x),4))