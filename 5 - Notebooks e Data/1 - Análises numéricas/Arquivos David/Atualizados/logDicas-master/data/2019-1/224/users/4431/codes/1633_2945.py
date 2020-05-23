from math import*
D=float(input("Digite o diametro da frigideira: "))
T=float(input("Digite a espessaura das panquecas: "))
P=float(input("Digite a quantidade de panquecas:"))
M=((D**2)*T*pi*P)/4
print(round(M,2))