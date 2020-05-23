from numpy import*

x = array(eval(input()), dtype = int)

z = zeros(7, dtype = int)
for i in range(7):
	z[i] = sum(x[:, i])
for i in range(7):
	if(max(z) == sum(x[:, i])):
		print(i + 1)