raio = float(input("digite o raio: "))

from math import * 

area = pi * raio ** 2 
volume = 4 / 3 * pi * raio ** 3

print("%.3f" % area)
print("%.3f" % volume)