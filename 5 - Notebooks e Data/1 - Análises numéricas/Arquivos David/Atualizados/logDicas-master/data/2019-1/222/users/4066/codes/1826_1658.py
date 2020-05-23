from numpy import*
v = input("Paises: ").split(',')

s = len(v)

z = zeros(s)

for i in range(s):
	for k in range(s):
		if v[i] == v[k]:
			z[i] = z[i] + 1
print(z)