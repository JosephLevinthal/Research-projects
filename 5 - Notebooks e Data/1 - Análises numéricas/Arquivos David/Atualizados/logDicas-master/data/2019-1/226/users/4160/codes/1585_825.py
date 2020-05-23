raio = float(input(" Digite o valor do raio: "))
from math import pi

area = pi * raio ** 2
volume = (4 * pi * raio ** 3) / 3
print(round(area,3))
print(round(volume,3))