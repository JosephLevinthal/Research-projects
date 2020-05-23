from numpy import*

x = array(eval(input("vetor media final: ")))
y = array(eval(input("vetor presenca: ")))
z = int(input("carga horaria: "))
n = zeros(3, dtype=int)

f = (3/4) * z
j = 0

for i in x:
	if (i >= 5) and (y[j] >= f):
		n[0] = n[0] + 1
		j = j + 1
	elif i < 5:
		n[1] = n[1] + 1
		j = j + 1
	elif y[j] < f:
		n[2] = n[2] + 1
		j = j + 1
print(n)
