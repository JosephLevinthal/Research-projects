from numpy import *
vetor = array(eval(input("digite o vetor: ")))
i = 0  #[1,5,6,-1,-2] ===> [1,5,6]
v = 0
while(i<size(vetor)):
	if(vetor[i]>=0):
		v = v + 1
	else:
		v = v + 0
	i = i + 1
i2 = 0
i3 = 0
z = zeros(v, dtype = int)
while(i3<v):
	if(vetor[i2] >= 0):
		z[i3] = vetor[i2]
		i2 = i2 + 1
		i3 = i3 + 1
	else:
		i2 = i2 + 1
		i3 = i3 + 0
print(z)




