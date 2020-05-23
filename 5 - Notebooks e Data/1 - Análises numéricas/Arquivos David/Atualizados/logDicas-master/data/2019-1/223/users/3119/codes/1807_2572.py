from numpy import*

m = array(eval(input("Digite as metriculas: ")))

x = 0

for i in range(size(m)):
	if(m[i] % 2 != 0):
		x = x + 1
	else:
		x = x
		
cont = zeros(x, dtype = int)
j = 0
for i in range(size(m)):
	if(m[i] % 2 != 0):
		cont[j] = m[i]
		j = j + 1
		
print(cont)		