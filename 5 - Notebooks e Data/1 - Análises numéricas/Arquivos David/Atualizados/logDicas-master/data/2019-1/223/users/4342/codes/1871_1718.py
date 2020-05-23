from numpy import *

N= array(eval(input("dimensao matriz:")))
coluna = int(input("coluna:"))
lin = int(input("linha:"))
casa = N[coluna, lin]
if (casa == "P"):
	print("PRETA")
elif(casa == "B"):
	print("BRANCA")
elif(casa == "V"):
	print("VAZIA")