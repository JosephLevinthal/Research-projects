import math
raio = float(input("numero"))
area_circulo = math.pi * raio**2
volume_esfera = (math.pi * raio**3) * 4/3
print(round(area_circulo, 3))
print(round(volume_esfera, 3))