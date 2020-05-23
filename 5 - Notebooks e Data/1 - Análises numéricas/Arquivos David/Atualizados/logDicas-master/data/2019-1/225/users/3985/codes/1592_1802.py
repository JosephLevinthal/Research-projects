c= float(input("Pontos de vida iniciais:"))
d1= float(input("Valor do dado 1:"))
d2= float(input("Valor do dado 2:"))

 
from math import*
x= (sqrt(5*d1)+pi*d2/3)
v= (c-x)
print(int(v))