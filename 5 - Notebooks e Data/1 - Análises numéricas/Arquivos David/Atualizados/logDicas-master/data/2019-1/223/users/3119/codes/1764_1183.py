from numpy import*

a = array(eval(input("Digite os numeros: ")))

p = 0
i = 0

while(i < size(a)):
	if(a[i] > 0):
		p = p + 1
	else:
		p = p + 0
	i = i + 1	
p	

aux = zeros(p, dtype = int)
j = 0
i = 0

while(i < size(a)):
	if(a[i] > 0):
		aux[j] = a[i]
		j = j + 1
	i = i + 1	

print(aux)



