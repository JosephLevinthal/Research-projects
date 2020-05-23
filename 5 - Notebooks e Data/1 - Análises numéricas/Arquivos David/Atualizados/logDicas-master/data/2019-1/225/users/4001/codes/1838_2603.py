from numpy import*
x = array(eval(input("Matriz: ")))
v = zeros(4, dtype=int)
for j in range(4):
	c = 0
	v = zeros(4, dtype=int)
	v = x[:,j]
	v = sorted(v, reverse=True)
	for i in range(4):
		x[i,j] = v[c]
		c = c + 1
print(x)
		