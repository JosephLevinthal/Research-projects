from math import*
a = float(input("distacia para arvore1:"))
b = float(input("distancia para arvore 2:"))
ang = radians(float(input( "angulo de a e b:")))
c = sqrt( a ** 2 + b ** 2 -(2 * a * b * cos(ang)))
print(round(c , 2))