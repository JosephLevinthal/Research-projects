import math

T = float(input("Periodo de oscilao: "))

G = 9.81
L = 9.81 * ((T)/(2*math.pi))**2

print(L)