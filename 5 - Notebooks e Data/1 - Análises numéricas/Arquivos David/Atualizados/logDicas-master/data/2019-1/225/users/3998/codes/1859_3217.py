from numpy import*

s = array(eval(input()), dtype = int)
t = size(s)
i = 0
m = zeros((t,2), dtype = int)
for c in range(t):
	p = int(input())
	m[c, 0] = s[i]
	m[c, 1] = p
	i += 1

print(m)
maior = max(m[:,1])
for i in range(t):
	if(maior == m[i,1]):
		print("O departamento que possui maior salario gerencial e ", m[i,0])