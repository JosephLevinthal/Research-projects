#R é o tamanho das rosquinhas em cm, r é o raio do tubo da rosquinha, Q é a quantidade de rosquiunhas
from math import pi
R=float(input("Tamanho das rosquinhas: "))
r=float(input("raio do tubo: "))
Q=float(input("Quantidades de rosquinhas: "))
M= 2*pi**2*R*r**2*Q
print(round(M, 2))