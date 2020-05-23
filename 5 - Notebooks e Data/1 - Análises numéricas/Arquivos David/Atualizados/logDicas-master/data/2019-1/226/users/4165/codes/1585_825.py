raio = float(input( "insira o raio"))
from math import *
val = pi
area = val*(raio**2)
volume = 4/3 * val * (raio**3)
print(round( area,3))
print(round( volume,3))