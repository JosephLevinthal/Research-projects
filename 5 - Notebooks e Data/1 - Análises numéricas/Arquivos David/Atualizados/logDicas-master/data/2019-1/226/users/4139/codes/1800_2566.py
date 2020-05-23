from numpy import*
vet = array(eval(input("Quantidade de faltas na semana: ")))

vf = zeros(7)

for x in range(size(vet)):
	if vet[x] == 2:
		vf[x] = vf[x] + 1
	for x in range(size(vt)):
		vf[x] = 

print(round(vf,1))
