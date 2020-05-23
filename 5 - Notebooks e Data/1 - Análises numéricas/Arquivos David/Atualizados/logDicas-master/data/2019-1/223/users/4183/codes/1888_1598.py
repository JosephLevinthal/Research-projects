from numpy import *
v = array(eval(input("Digite um vetor: ")))
x = 0
for i in range(size(v)):
	if (v[i] > 80):
		v[i] = v[i] - 5
x = sum(v)
print(round(x,2))
	