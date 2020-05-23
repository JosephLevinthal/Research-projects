from numpy import*

m=array(eval(input("quantas horas?")))
n=shape(m)[0]
v = zeros((n), dtype=int)

for i in range(shape(m)[0]):
	cont = 0
	for j in range(7):
		cont=cont+m[i,j]
		v[i] = cont
print(v)