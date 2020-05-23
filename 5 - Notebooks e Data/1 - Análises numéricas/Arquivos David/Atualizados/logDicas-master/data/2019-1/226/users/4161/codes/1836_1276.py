from numpy import*

m = array(eval(input("horario de funcionarios: ")))

o = shape(m)[1]
v = zeros((o), dtype=int)
for i in range(o):
	v[i] = sum(m[:,i])
i = 1
for x in v:
	if x == max(v):
		print(i)
		i = i + 1
	else:
		i = i + 1

		