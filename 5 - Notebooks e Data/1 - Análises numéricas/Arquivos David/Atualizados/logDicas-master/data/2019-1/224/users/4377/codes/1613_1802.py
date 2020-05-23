pontos=int(input("pontosinicias"))
sorteio1=int(input("sorteio1"))
sorteio2=int(input("sorteio2"))
from math import*
dano1=int(((5*sorteio1)**0.5+pi**(sorteio2/3)))
dano2=((5*sorteio2)**0.5+pi**3)
danos=dano1+dano2
total=pontos-dano1
print(total)