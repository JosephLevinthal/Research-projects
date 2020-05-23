from numpy import*

p = array(eval(input("presenca: ")))
f = array(eval(input("faltosos: ")))

z = zeros(12, dtype=int)
i = 0
m = 0

while i < 12:
	if z[i] != max(z):
		m = m
	else:
		m = i + 1
	z[i] = p[i] - f[i]
	i = i + 1
print(m)