#exportamos pi do math
from math import *
#definmos a variavel do raio 
raio=float(input("raio"))
#definimos o valor da area e do volume
area=pi*raio**2
volume=4/3*pi*raio**3
#arrendodamos 
areaar=round(area, 3)
volumear=round(volume, 3)
print(areaar)
print(volumear)