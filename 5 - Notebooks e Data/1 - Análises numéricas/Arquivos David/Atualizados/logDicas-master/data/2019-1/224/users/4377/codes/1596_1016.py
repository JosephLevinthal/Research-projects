l1=float(input("comprimentoa"))
l2=float(input("comprimentob"))
l3=float(input("comprimentoc"))
s=(l1+l2+l3)/2
from math import*
area = sqrt(s*(s-l1)*(s-l2)*(s-l3))
print(round(area,5))