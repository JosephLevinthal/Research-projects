xa= float(input("coordenada xa: "))
ya= float(input("coordenada ya: "))
xb= float(input("coordenada xb: "))
yb= float(input("coordenada yb: "))

d= ((xb - xa ) ** 2 + (yb - ya) ** 2) ** (1 / 2) 
print(round(d, 3))