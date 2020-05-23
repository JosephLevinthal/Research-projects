xa=float(input("Coordenada ponto Xa: "))
ya=float(input("Coordenada ponto Ya: "))
xb=float(input("Coordenada ponto Xb: "))
yb=float(input("Coordenada ponto Yb: "))

a=(xa, ya)
b=(xb, yb)

xm=(xb+xa)/2
ym=(yb+ya)/2

print(round(xm,2))
print(round(ym,2))