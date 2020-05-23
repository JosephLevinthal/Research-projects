from numpy import*
v = array(eval(input("turmas: ")))
q = 0
for x in v:
	if x%2 == 0:
		q = q + 1
print(q)
v0 = zeros(q,dtype=int)
a = 0
n = size(v)
for x in range(n):
	if v[x]%2 == 0:
		v0[a] = x
		a = a + 1
print(v0)