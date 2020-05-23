from numpy import*
a = array(eval(input("matriculas:")))
b = 0
for y in a:
	if (y%2 !=0):
		b = b+ 1
p = zeros(b, dtype=int)
x = 0 
g = 0
for r in a:
	if r%2 != 0:
		p[x] = a[g]
		x = x + 1
	g = g + 1
print(p)







