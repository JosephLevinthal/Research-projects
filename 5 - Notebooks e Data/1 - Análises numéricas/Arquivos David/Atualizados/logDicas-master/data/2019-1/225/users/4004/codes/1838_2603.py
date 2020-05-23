from numpy import*

m = array(eval(input()))

for j in range(4):
	v = zeros(4)
	k = 0
	for i in range(4):
		v[k] = m[i,j]
		k += 1
	v = sorted(v, reverse = True)
	k = 0
	for i in range(4):
		m[i,j] = v[k]
		k += 1

print(m)