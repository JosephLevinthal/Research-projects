from numpy import*
b = array(eval(input("Digite o numero de funcionarios: ")))
v = zeros(shape(b)[1])
for i in range(shape(b)[1]):
	v[i] = sum(b[:,i])
maximo = max(v)
for i in range(size(v)):
	if(v[i]==maximo):
		print(i+1)