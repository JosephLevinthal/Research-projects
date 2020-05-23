from numpy import*

x = (input("paises;")).split(',')

z = zeros(5,dtype = int)

for i in range(size(x)):
	if x[i] == 'BE':
		z[0] = z[0] + 1
	
	elif x[i] == 'ES':
		z[1] = z[1] + 1
	
	elif x[i] == 'FR':
		z[2] = z[2] + 1
		
	elif x[i] == 'IT':
		z[3] = z[3] + 1
		
	elif x[i] == 'PT':
		z[4] = z[4] + 1 	
d = max(z)
print(d)
print(z)	