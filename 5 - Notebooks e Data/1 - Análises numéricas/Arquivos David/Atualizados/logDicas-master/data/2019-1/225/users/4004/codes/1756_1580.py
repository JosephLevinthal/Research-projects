from numpy import *

n = array(eval(input("notas: ")))
k = array(eval(input("Nomes: ")))

f = 0 #faltas
a = 0 #aprovados
r = 0 #reprovados
s = 0 #soma
i = 0 #contador 1
l = 0 #contador 2
while i < size(n):
	if n[i] == max(n):
		l = i
	else:
		l = l
	if n[i] < 0:
		i = i + 1
		f = f + 1
	else:
		if n[i] >= 6:
			a = a + 1
			s = s + n[i]
			i = i + 1
		else:
			r = r + 1
			s = s + n[i]
			i = i + 1
b = a + r
b = arange(b)
m = s/size(b)
print(f)
print(a)
print(r)
print(round(m, 2))
print(k[l])