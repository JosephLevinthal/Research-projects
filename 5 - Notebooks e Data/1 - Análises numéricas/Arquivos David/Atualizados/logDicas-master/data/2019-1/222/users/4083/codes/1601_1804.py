xa = float(input("Digite a coordenada xa"))
ya = float(input("Digite a coordenada ya"))
xb = float(input("Digite a coordenada xb"))
yb = float(input("Digite a coordenada yb"))

dab = ((xb - xa)**2 + (yb - ya)**2)**(1/2)
print(round(dab, 3))