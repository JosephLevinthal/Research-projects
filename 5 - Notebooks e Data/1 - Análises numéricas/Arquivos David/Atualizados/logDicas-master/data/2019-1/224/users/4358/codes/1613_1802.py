from math import*
pvo=int(input("Digite os potos de vida inicial:"))
d1=int(input("digite de 1 a 20:"))
d2=int(input("digite de 1 a 20:"))
dano=((5*d1)**0.5)+(pi**(d2/3))
cai=pvo-(int(dano))
print(cai)