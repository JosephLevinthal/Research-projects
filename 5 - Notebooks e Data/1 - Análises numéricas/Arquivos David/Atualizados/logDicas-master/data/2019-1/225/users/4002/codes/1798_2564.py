from numpy import*
g = array(eval(input("Gols: ")))
a = array(eval(input("Gols adversarios: ")))

v = 0
e = 0
d = 0
V = zeros(3, dtype=int)

for i in range(size(g)):
	if (g[i] > a[i]):
		v = v + 1
		V[0] = v
	elif (g[i] == a[i]):
		e = e + 1
		V[1] = e
	elif (g[i] < a[i]):
		d = d + 1
		V[2] = d
print(V)