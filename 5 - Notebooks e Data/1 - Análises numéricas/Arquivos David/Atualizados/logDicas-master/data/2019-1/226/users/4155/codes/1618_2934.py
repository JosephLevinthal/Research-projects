from math import *

q0 = float(input("valor:"))
r = float(input("taxa anual:"))
qf = 3 * q0

y = (log(qf) - log(q0)) / r 
t = int(y) + 1

print(t)