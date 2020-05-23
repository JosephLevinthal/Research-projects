from numpy import *
# Vetor contendo o nome dos meses do ano
y = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
x = input()

a = (x[:2])
b = int((x[2:4]))
c = (x[4:8])
d = 0

h = 0

while size(y) != h:
	if b == h:
		d = y[h-1]
	h += 1

print(a,"de",d,"de",c)
