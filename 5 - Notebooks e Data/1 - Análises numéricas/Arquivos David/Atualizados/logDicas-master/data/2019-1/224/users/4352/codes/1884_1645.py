from numpy import*
s = array(eval(input("digite o vetor com os saques: ")))
cont = 0
for i in s:
	if i >= 2000:
		cont = cont + 1
z = zeros(cont,dtype=int)
cont2 = 0
cont3 = 0
for j in s:
	if j >= 2000:
		z[cont2] = cont3
		cont2 = cont2 + 1
	cont3 = cont3 + 1
print(cont)
print(z)