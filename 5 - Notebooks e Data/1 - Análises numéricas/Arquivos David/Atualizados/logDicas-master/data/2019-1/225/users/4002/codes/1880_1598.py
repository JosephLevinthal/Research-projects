from numpy import*

v = eval(input("Valor: "))

for i in range(len(v)):
	if v[i]>80:
		v[i]-=5
custo = float(sum(v))

print(round(custo, 2))