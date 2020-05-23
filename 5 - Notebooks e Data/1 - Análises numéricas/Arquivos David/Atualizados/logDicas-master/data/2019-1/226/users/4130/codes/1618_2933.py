from math import *

x = float(input("Valor de Q0: "))
y = float(input("Valor final de Qf: "))
z = int(input("Anos de investimento: "))

r = (log(y) - log(x)) / z

print(r)