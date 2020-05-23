from numpy import*

v = array(eval(input("digite: ")))
i = 0
a = size(v)
c = 0

while	(i != a):
		c = c + v[i]**(1/3)
		i = i + 1
		
g = (c/a)**3
print(round(g, 2))