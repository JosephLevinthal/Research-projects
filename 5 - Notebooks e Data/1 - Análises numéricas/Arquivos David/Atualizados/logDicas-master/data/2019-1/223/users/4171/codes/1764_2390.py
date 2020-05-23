from numpy import *

pmes = array(eval(input("presentes por mes: ")))
fmes = array(eval(input("faltantes por mes: ")))

g = arange(size(pmes), dtype = int)

i = 0
k = 1
h = 1

while i < size(g):
		
	g[i] = pmes[i] - fmes[i]
		
	if g[i] < max(g):
		
		k += 1
	else:
		h += 1
		
	i += 1

print(h)