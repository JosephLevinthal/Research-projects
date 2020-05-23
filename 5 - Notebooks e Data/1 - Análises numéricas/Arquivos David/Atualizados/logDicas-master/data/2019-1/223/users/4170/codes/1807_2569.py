from numpy import*
x = array(eval(input("Vetor de numeros: ")))
m = sum(x)/size(x)

for i in range(size(x)):
	t = sum((x[i] - m)**2)
	d = ((t) / (size(x) - 1))**0.5
print(round(d,3))	