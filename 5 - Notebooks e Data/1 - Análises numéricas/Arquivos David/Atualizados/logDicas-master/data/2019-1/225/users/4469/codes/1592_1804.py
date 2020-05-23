import math

xa = float(input("XA: "))
ya = float(input("YA: "))
xb = float(input("XB: "))
yb = float(input("YB: "))

dab = math.sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))

print(round(dab, 3))