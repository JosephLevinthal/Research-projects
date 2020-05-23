y1=float(input( ))
y2=float(input( ))
x1=float(input( ))
x2=float(input( ))

from math import*

formula=float((x2-x1)**2+(y2-y1)**2)
distancia=float(sqrt(formula))

dab=round(distancia, 3)
print(dab)