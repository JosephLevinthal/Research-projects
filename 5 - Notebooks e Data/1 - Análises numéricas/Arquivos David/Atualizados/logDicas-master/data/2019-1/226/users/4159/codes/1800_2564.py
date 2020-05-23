
n = 0
vi = 0
d = 0
e = 0
for i in v:
	if(i>g[n]):
		vi=vi+1
	elif(i<g[n]):
		d=d+1
	else:
		e=e+1
	n=n+1
b = zeros(3, dtype=int)
b[0] = vi
b[1] = e
b[2] = d
print(b)