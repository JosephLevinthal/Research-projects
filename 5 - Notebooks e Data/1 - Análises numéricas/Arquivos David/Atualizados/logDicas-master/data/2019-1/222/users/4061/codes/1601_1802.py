from math import *
#from numpy.random import *
vida = int(input("digite vida"))
D1 = int(input("dado 1"))#randint(1, 20, size = 1)
D2 = int(input("dado 2"))#randint(1, 20, size = 1)
dano = (sqrt(5*D1))+(pi**(D2/3))
print(vida-int(dano))
