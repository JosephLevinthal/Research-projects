from numpy import *

v = array(eval(input("Matriculas: ")))

a = 0

for x in v:
	if(x % 2 != 0):
		a = a + 1
p = zeros(a, dtype = int)

y = 0
j = 0

for x in v:
	if(x % 2 != 0):
		p[y] = v[j]
		y = y + 1
	j = j + 1
print(p)