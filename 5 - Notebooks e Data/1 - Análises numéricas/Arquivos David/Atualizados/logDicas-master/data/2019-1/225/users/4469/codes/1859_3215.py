from numpy import *

a = array(eval(input()), dtype = int)
t = size(a)
i = 0
m = zeros((t,2), dtype = int)
for c in range(t):
	p = int(input())
	m[c, 0] = a[c]
	m[c, 1] = p
	
print(m)
b = max(m[:,1])
for i in range(t):
	if(b == m[i,1]):
		print("O aluno que possui o maior numero de faltas e o", m[i,0])
		break