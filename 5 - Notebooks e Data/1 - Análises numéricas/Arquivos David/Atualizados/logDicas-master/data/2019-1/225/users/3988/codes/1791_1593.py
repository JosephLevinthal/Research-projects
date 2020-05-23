from numpy import*
v = array(eval(input("entrada:")))
t = 1 
c = 0
q = size(v)
s = 0
f = 0
g = 0
while(q>c):
	r = v[s] * t
	s = s + 1
	g = g + t
	t = t + 1
	c = c + 1
	f = f + r
y = f / g
print(round(y, 2))
