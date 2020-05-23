xa =  float(input("Informe a coordenada X de A"))
ya =  float(input("Informe a coordenada y de A"))
xb =  float(input("Informe a coordenada X de B"))
yb =  float(input("Informe a coordenada Y de B"))
from math import*
dab = (xb-xa)**2 + (yb-ya)**2
print(round(sqrt(dab),3))