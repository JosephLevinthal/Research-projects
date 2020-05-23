from numpy import*

n = array(eval(input("Notas do aluno:")))
r = 0 #contador pros reprovados
for i in range(size(n)):
	if n[i] < 5.0:
		r = r + 1


print(r)
d = zeros(r, dtype = int)
a = 0
b = 0

for j in range(size(n)):
	if n[j] < 5:
		d[a] = j
		a = a+1
	b = b + 1
print(d)