# Coordenadas do ponto A (xa, ya)
xa = float (input(" Digite a coordenada xa: "))
ya = float(input("Digite a coordenada ya: "))

# Coordenadas do ponto B (xb, yb)
xb = float (input(" Digite a coordenada xb: "))
yb = float(input("Digite a coordenada yb: "))


# Calcular o ponto médio (xm, ym):
xm = (xb + xa)/ 2
ym = (yb + ya)/ 2 

print(round(xm ,1))
print(round(ym ,1))