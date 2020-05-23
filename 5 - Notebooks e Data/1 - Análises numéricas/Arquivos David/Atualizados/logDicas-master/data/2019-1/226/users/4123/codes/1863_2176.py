from numpy import*
mtz = array(eval(input()))
tam = shape(mtz)[0]
x = y = 0
z = mtz[0,1]
for x in range(0,tam):
	for y in range(0,tam):
		if mtz[x,y]>=z and x!=y:
			z = mtz[x,y]
print(z)