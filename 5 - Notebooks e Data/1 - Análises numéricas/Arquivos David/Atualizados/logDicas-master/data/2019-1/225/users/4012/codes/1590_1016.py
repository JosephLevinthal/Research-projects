l1 = float(input("Digite lado 1: "))
l2 = float(input("Digite lado 2: "))
l3 = float(input("Digite lado 3: "))

s = (l1 + l2 + l3) / 2

from math import *

A = sqrt(s * (s - l1) * (s - l2) * (s - l3))

print("%.5f" % A)