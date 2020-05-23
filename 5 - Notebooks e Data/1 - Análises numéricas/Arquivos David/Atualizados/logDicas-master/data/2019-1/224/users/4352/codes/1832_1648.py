from numpy import*
vi = array(eval(input("digite as aulas frequentadas: ")))
cont = 0
for i in range(size(vi)):
	if vi[i] < 70:
		cont = cont + 1
print(cont)
z = zeros(cont, dtype=int)
contt = 0
for j in range(size(vi)):
	if vi[j] < 70:
		z[contt] = j
		contt = contt + 1
print(z)