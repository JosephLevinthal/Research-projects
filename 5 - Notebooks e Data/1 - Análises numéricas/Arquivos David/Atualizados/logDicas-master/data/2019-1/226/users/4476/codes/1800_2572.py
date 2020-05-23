from numpy import *

v = array(eval(input("dgt: ")))

x = 0

for i in v:
	if (i % 2) != 0:
		x = x + 1
g = zeros(x, dtype=int)

a = 0
b = 0

for r in v:
	if (r % 2) != 0:
		g[a] = v[b]
		a = a + 1
	b = b + 1
print(g)