import math
Hp=int(input())
D1=int(input())
D2=int(input())
Dano=((5*D1))**(0.5)+(math.pi**(D2/3))
resto= Hp-int(Dano)
print(resto)