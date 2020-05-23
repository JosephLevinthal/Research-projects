import math
var1=int(input("pontos de vida: "))
d1=int(input("dado1:"))
d2=int(input("dado2:"))
a=((5*d1)**(0.5))+(math.pi**(d2/3))
resto=var1-int(a)
print(resto)