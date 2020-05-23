from numpy import*

p = array(eval(input("Frequencia: ")))
f = array(eval(input("Frequencia: ")))

s = size(p)

d = zeros(s, dtype=int)

for i in range(s):
	d[i] = p[i] - f[i]

for p in range(s):
	if d[p] == max(d):
		print(p+1)