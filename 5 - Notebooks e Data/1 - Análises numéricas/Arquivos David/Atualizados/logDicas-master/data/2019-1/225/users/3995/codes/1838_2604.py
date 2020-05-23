from numpy import*
h=array(eval(input("digite o numero de funcionarios")))
for i in range(shape(h)[0]):
	print(max(h[i,:]))