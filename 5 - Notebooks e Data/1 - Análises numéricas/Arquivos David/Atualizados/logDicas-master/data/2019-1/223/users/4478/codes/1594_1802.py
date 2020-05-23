Vida = int(input("Ponto de vida inciais: "))
D1 = int(input("D1: "))
D2 = int(input("D2: "))

import math

dano =int(math.sqrt(5*D1)+math.pi**(D2/3)) 
Restantes = Vida - dano
print(Restantes)