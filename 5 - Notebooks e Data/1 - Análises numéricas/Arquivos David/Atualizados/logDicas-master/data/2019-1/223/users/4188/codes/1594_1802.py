P=int(input("pontos de vidas iniciais: "))
D1=int(input("lancamento D1: "))
D2=int(input("lancamento D2: "))
from math import pi
dan=((5*D1)**(1/2)) + (pi)**(D2/3)
s=P-int(dan)
print(s)