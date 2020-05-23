from numpy import *

v = array(eval(input("insira as notas:")))

reprov = 0
for i in range(size(v)):
	if(v[i] < 5):
		reprov = reprov + 1
print(reprov)		
cont = zeros(reprov,dtype = int)
j = 0
y = 0
for i in range(size(v)):
	if(v[i] < 5):
		cont[j] = y
		j = j + 1
	y = y + 1

print(cont)
		
	