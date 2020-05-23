from numpy import*

v = array(eval(input("notas: ")))
aux = 0

for i in range(size(v)):
	if v[i]>=5:
		aux = aux + 1 
print(aux)

d = zeros(aux, dtype=int)
j=0
for i in range(size(v)):
	if v[i] >= 5:
		d[j] = i
		j = j+ 1
print(d)
		
	

		