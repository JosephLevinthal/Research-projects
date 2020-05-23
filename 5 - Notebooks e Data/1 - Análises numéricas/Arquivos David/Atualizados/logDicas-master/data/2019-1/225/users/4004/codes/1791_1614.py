from numpy import*

a = array(eval(input("vetor de nomes de alimentos: ")))
q = array(eval(input("vetor de quantidades: ")))
k = array([0.97,2.95,1.27,1.04,0.2])

i = 0
s = size(a)
r = zeros(s, dtype=float)

while i < s:
	if a[i] == "BANANA":
		r[i] = k[0] * q[i]
		i = i + 1
	elif a[i] == "BIFE":
		r[i] = k[1] * q[i]
		i = i + 1
	elif a[i] == "FEIJOADA":
		r[i] = k[2] * q[i]
		i = i + 1
	elif a[i] == "OMELETE":
		r[i] = k[3] * q[i]
		i = i + 1
	else:
		r[i] = k[4] * q[i]
		i = i + 1
t = sum(r)
print(round(t, 2))