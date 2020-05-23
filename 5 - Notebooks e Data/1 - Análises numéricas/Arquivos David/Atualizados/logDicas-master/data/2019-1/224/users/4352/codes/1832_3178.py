from numpy import*
v = array(eval(input("digite o vetor: ")))
z = zeros(size(v), dtype=int)
for i in v:
	if i != 0:
		z[0] = z[0] * 1
print(z)