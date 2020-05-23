from numpy import*
v = array(eval(input("digite as matriculas dos alunos: ")))
cont = 0
for i in v:
	if (i % 2 != 0):
		cont = cont + 1
a = zeros(cont, dtype=int)
contt = 0
for j in v:
	if (j % 2 != 0):
		a[contt] = j
		contt = contt + 1
print(a)