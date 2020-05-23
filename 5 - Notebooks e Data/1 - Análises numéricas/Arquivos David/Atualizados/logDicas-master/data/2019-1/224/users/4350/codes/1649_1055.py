import math
v = float(input("velocidade inicial"))
a = math.radians(float(input("angulo")))
d = float(input("distancia"))
g = 9.8
r = (v**2) * math.sin(2*a) / g
if abs(r-d) <= 0.1:
	print("sim")
else:
	print("nao")
