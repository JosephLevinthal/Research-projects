import math
a= float(input("Qual o periodo de oscilacao do Pendulo? "))
b= (a/(2*math.pi))
c= (b ** 2)
g= float(9.81)
d= g*c
print(d)