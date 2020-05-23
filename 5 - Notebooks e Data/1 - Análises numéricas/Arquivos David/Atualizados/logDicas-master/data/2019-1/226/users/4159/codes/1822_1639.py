from numpy import*
v = array(eval(input("numero de alunos: ")))
c = 0
x = 0
for i in range(size(v)):
	if((v[i]%2)==0):
		c = c + 1 
g = zeros(c, dtype=int)
for d in range(size(v)):
	if((v[d]%2)==0):
			g[x] = d
			x = x+1
print(c)
print(g)
	