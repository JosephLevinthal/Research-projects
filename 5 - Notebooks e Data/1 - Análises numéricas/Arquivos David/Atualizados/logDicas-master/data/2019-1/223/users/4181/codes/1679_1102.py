from math import *
altura_total = float(input())
nivel = float(input())
raio = float(input())

if(altura_total >0 and nivel >0 and raio >0 and altura_total>nivel and altura_total>2*raio):
	calota = pi/3 * altura_total**2 * (3*raio - altura_total) *1000
	volume = 4/3 * pi * raio**3 *1000 - calota
	a = (pi*raio**2) * altura_total - calota
	print(round(a,3))