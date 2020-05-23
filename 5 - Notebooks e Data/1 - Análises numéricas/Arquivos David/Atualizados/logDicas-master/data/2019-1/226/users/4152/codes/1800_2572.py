from numpy import *
vet = array(eval(input("Vetor de metriculas: ")))
b = 0
for i in vet:
	if (i % 2 != 0):
		b = b + 1
p = zeros(b, dtype=int)
x = 0
g = 0
for r in vet:
   if (r % 2 != 0):
	   p[x] = vet[g]
	   x = x + 1
   g = g + 1
print(p)
	