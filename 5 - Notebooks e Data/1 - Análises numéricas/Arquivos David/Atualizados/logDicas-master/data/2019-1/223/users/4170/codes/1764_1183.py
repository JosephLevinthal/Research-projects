from numpy import*
v =  array(eval(input("Vetor: ")))
p = 0
i = 0
while(i < size(v)):
	if(v[i] > 0):
		p = p + 1
	else:
		p = p + 0
	i = i + 1
p
aux = zeros(p, dtype=int)
j = 0
i = 0
while(i < size(v)):
	if(v[i] > 0):
		aux[j] = v[i]
		j = j + 1
	i = i + 1
print(aux)	