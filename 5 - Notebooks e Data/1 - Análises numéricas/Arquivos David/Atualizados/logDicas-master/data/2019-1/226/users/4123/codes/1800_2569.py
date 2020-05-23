from numpy import*
vet = array(eval(input()))
m = sum(vet)/size(vet)
soma = 0
for x in vet:
	soma += (x-m)**2
d = (soma/(size(vet)-1))**0.5
print(round(d,3))