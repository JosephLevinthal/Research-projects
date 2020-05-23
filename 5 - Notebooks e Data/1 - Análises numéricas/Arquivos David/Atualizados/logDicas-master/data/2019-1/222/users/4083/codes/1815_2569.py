from numpy import*
a = 0
v = array(eval(input("Digite o vetor: ")))
b = sum(v)/size(v)
for i in range(size(v)):
	a = a + (v[i] - b)**2

	print(v[i])