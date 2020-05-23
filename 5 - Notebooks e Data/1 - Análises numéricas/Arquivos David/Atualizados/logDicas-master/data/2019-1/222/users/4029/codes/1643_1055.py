import math
v= float(input("Velocidade inicial: "))
a= float(input("Angulo: "))
d= float(input("Distancia entre o passaro e o porco: "))
x= 2 * a
g= 9.8
r= (((v ** 2) * (math.radians((math.sin(x)))/ g)
var=abs (d-r)	  
if ( var < 0.1 ):
	  p= "SIM"
else:
	  p= "NAO"
print(p)