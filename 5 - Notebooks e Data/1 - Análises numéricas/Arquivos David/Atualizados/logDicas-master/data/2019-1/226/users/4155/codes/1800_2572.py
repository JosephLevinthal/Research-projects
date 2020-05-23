from numpy import*
x = array(eval(input("x: ")))
y = 0
for i in x:
	if (i%2!=0):
		y=1+y
p = zeros(y, dtype=int)
u = 0
o = 0
for t in x:
	if t%2 !=0:
		p[u] = x[o]
		u=1 + u
	o=1 + o
print(p)