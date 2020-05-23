#coordenadas do ponto a
xa=float(input("coordenada de xa"))
ya=float(input("coordenada de ya"))
#coordenadas do ponto b
xb=float(input("coordenada de xb"))
yb=float(input("coordenada de yb"))
#variavel da distancia
d=(((xb-xa)**2)+((yb-ya)**2))**0.5
rd= round(d, 3)
print(rd)