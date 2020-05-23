#Arte Ascii 2
from numpy import*
ast=int(input("Numero de asteristicos: "))#Número de asteristicos

for i in range(ast,0,-1):# Primeira parte
	x = i*"*"+2*(ast-i)*"o"+i*"*"
	print(x)
	