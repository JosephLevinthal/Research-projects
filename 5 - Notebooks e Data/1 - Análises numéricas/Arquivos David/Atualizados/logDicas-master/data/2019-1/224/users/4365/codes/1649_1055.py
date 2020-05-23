from math import*
v0=float(input("velocidade inicial: "))
ang= radians(float(input("angulo alfa: ")))
d=float(input("distancia porco-passaro: "))
g==9.8
R=(v0**2)*(sin(2*radians(ang)/))/g

if (abs(d-R)<0.1):
    print("sim")
else:
    print("nao")