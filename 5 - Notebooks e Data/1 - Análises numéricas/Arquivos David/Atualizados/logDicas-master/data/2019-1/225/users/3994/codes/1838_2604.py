from numpy import*
m = array(eval(input("Digite o numero de funcionarios: ")))
for i in range(shape(m)[0]):
	print(max(m[i,:]))