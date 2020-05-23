from math import * 
t1 = radians(float(input(" Digite a latitude t1 de um ponto P1: ")))
g1 = radians(float(input(" Digite a longitude g1 de um ponto P1: ")))
t2 = radians(float(input(" Digite a latitude t2 de um ponto P2: ")))
g2 = radians(float(input(" Digite a longitude g2 de um ponto P2: ")))
 
R = 6371.01   

d = R * acos(sin(t1)* sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print(round(d,2))