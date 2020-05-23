from math import*

hp = int(input())
d1 = int(input())
d2 = int(input())

hpzin = hp - int((5*d1)**(1/2)+pi**(d2/3))
print(hpzin)