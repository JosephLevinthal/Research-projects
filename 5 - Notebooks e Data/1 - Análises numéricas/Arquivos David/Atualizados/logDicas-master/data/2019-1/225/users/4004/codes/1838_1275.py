from numpy import*

x = array(eval(input("valores: ")), dtype = int)

z = zeros(shape(x)[0], dtype = int)
for i in range(shape(x)[0]):
	z[i] = sum(x[i,:])
	
print(z)