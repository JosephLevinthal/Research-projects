from numpy import *
start = input("Digite a palavra Calcule: ")

if(start == "Calcule"):
	h = 0
	for i in range(50):
		h = h + ((2*i + 1)/(1+i))
	print(round(h, 2))		