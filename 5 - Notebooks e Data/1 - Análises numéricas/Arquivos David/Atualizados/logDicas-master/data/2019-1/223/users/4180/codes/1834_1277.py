from numpy import *
from numpy.linalg import *



cityA = int(input("digite cidade A:"))
cityB = int(input("digite cidade B:"))

cityA = (cityA % 10) - 1
cityB = (cityB % 10) - 1

print(distancia_city[cityA,cityB])