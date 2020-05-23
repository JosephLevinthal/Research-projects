x1 = float(input("insira a coordenada de x1:"))
y1 = float(input("insira a coordenada de y1:"))
x2 = float(input("insira a coordenada de x2:"))
y2 = float(input("insira a coordenada de y2:"))

dx = (x2 - x1)**2
dy = (y2 - y1)**2

dab = (dx + dy)**0.5
print(round(dab,3))