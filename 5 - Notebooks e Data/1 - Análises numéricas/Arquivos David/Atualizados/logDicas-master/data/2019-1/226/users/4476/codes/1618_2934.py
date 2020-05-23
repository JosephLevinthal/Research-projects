vi = float(input("valor investido: "))
r = float(input("taxa de rendimento: "))
from math import *
vf = vi*3
y = (log(vf) - log(vi)) / r
print(int(y + 1))
