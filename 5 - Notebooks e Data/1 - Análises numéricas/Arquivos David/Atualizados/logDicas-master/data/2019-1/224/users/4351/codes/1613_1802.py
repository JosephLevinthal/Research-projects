from math import*
vida=int(input("pontos de vida"))
D1=int(input("valor sorteado d1"))
D2=int(input("valor sorteasdo d2"))
dano=int((5*D1)**(1/2)+pi**(D2/3))
vidasobra= vida-dano
print(vidasobra)