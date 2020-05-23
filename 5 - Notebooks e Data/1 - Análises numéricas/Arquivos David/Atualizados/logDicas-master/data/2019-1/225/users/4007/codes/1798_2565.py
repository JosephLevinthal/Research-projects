from numpy import*
m = array(eval(input("media dos alunos: ")))
f = array(eval(input("presenca: ")))
c = int(input("carga horaria: "))* 75 / 100
v = zeros(3, dtype=int)

i = 0
while (i < size(m)):

	if (m[i] >= 5) and (f[i] >= c):
		v[0] = v[0] + 1
		
	elif (m[i] < 5) and (f[i] >= c):
		v[1] = v[1] + 1
		
	elif (m[i] >= 5) and (f[i] < c):
		v[2] = v[2] + 1
		
	i = i + 1
print(v)
		