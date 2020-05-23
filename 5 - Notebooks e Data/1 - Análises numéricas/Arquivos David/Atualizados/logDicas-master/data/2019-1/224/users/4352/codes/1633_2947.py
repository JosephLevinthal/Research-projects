b = float(input("digite o valor do lado b: "))
c = float(input("digite o valor do lado c: "))
ang = float(input("digite o angulo de alfa: "))

from math import *
a = b**2 + c**2 - 2 * b * c * (cos(radians(ang)))
resultado = sqrt(a)
print(round(resultado, 2))