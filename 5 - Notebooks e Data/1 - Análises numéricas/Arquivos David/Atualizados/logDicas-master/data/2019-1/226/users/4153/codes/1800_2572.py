from numpy import *
v = array(eval(input("Insira: ")))
x = 0
for i in range(size(v)):
	if(v[i]%2 != 0):
		x = x + 1

g2 = zeros(x, dtype=int)
ni = 0
for r in range(size(v)):
	if(v[r]%2 != 0):
		g2[ni] = v[r]
		ni = ni + 1
print(g2)