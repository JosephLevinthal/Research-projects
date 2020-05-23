import math
xa = float(input("xa: "))
ya = float(input("ya: "))
xb = float(input("xb: "))
yb = float(input("yb: "))

d = math.sqrt((xb-xa)**2 + (yb-ya)**2)

print(round(d,3))