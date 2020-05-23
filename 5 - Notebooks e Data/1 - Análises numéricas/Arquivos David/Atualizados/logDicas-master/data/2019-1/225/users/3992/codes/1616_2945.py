from math import*
D = float(input("diametro da frigideira:"))
T = float(input("espessura da panqueca:"))
P = float(input("quantidade de panquecas"))
M = ((D**2) * T * pi * P)/4 
print(round(M, 2))