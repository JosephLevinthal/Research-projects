from numpy import *
v = array(eval(input("Digite o vetor de custos: ")))
i = 0
soma1 = 0
desc = 15 / 100
s = 0
a = 0
c = 0
tf = zeros(int(size(v)), dtype=int)
while (i < size(v)):
	if (v[i] >= 80.0):
		soma1 = soma1 + v[i] * desc
	i = i + 1
while (s < size(v)):
	if (v[a] >= 80.0):
		c = tf[a]
	s = s + 1
d = (sum(v) - sum(c)) + soma1
print(round(d, 2))