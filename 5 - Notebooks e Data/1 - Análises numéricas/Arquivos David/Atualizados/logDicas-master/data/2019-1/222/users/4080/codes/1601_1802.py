#ponto de vida inicial
hp1 = int(input("hp "))
#valores dos dados lançados 
D1 = int(input("primeiro dado: "))
D2 = int(input("segundo dado: "))
#formula de importação
from math import*
dano = sqrt(5*D1)+pi**(D2/3)
hp2 = int(hp1-dano)
print(hp2+1)

