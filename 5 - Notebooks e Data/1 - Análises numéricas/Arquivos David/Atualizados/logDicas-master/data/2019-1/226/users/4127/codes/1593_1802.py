from math import*
vida=int(input("vida inicial do monstro: "))
d1=int(input("qual valor do dado 1? "))
d2=int(input("qual valor do dado 2? "))



dano=((sqrt(5*d1))+pi**(d2/3))
print(vida-int(dano))
