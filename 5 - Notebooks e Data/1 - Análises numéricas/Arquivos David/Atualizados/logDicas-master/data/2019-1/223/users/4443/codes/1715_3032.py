from math import *
#Leitura do valor de x
x = float(input("Digite um valor para x: "))

if(x <= 0):
	print(round(0, 4))
elif(0 < x <= 1):
	print(round(1, 4))
elif(1 < x <= 2):
	print(round(x**(1/2), 4))
elif(x > 2):
	print(round(x**(1/3), 4))