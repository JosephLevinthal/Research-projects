from numpy import*
v = array(eval(input("digite um vetor de numeros inteiros: ")))
cont = 0
for i in v:
	if i == 1:
		cont = cont + 1
z = ones(size(v), dtype=int)
cont = 0
for j in v:
	if j != 1:
		z[cont] = j
		cont += 1
print(z)
	
		
	