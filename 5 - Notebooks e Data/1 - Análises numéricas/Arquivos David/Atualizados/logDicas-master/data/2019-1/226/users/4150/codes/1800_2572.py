from numpy import*

v = array(eval(input("digite: ")))

aux = 0

for i in range(size(v)):
	if v[i] % 2 != 0:
		aux = aux + 1

p = zeros(aux, dtype=int)

x = 0
g = 0 

for r in v:
	if (r%2 != 0):
		p[x] = v[g]
		x = x+1
	g = g+1
print(p)
	