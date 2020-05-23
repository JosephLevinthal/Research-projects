from numpy import*

m = array(eval(input("Matricula dos alunos:")))
impar = 0
for i in m:
	if i%2 != 0:
		impar = impar + 1
tm = zeros(impar, dtype=int)
a = 0
b = 0
for j in m:
	if j%2 != 0:
		tm[a] = m[b]
		a = a + 1
	b = b + 1
print(tm)
