from numpy import *
v = array(eval(input("Faltas: ")))
b = 0
for y in v:
	if(y%2 != 0):
		b = b + 1
p = zeros(b, dtype = int)
x = 0
g = 0
for r in v:
	if(r % 2!=0):
		p[x] = v[g]
		x = x + 1
	g = g + 1
print(p)
	
