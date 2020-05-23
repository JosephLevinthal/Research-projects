from math import*

life = int(input())
d1 =  int(input())
d2 =  int(input())

dano = sqrt(5*d1) + (pi**(d2/3))
result  = int(life - dano)
print(result+1)