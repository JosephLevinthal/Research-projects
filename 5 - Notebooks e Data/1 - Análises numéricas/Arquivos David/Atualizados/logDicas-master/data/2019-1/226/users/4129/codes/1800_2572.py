from numpy import*
m = array(eval(input("Matriculas: ")))

s = 0

for x in range(size(m)):
	if (m[x]%2 != 0):
		s = s + 1
g2 = zeros(s, dtype=int)
g = 0
b = 0

for a in range(size(m)):
	if(m[a]%2 != 0):
		g2[b] = m[a]
		b = b + 1
	g = g  + 1 
print(g2)