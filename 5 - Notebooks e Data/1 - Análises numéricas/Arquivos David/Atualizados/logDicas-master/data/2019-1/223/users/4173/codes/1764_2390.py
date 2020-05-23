from numpy import*
pmes = array(eval(input()))
fmes = array(eval(input()))
g = arange(size(pmes))
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