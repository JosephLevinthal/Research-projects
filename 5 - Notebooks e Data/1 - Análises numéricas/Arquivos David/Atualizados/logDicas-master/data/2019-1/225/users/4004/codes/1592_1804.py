xA = float(input(" "))
yA = float(input(" "))
xB = float(input(" "))
yB = float(input(" "))

Vx = (xB - xA) ** 2
Vy = (yB - yA) ** 2
dAB = (Vx + Vy) ** 0.5

print(round(dAB, 3))