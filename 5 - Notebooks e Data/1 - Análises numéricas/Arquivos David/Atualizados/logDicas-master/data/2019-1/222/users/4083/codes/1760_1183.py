from numpy import*

v = array(eval(input("v: ")))
print(v)

a = size(v)
i = 0
d = arange(a)
d = zeros(a)
k =0

while (i != a):
		if	(v[i] > 0):
			d = (v[i])
			k = k + 1

		i = i + 1

g = arange(k)
g = zeros(k)


y = 0
r = 0

while	(y != k):
		if (v[r] > 0):
			g = v[r]
			r = r + 1
		y = y + 1
print(g)