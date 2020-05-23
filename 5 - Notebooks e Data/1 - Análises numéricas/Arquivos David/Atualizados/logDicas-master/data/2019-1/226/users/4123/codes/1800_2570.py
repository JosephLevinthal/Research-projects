from numpy import*
vet = array(eval(input()))
m = sum(vet)/size(vet)
soma = 1
for x in vet:
	soma = soma*abs(x-m)
d = (soma)**(1/size(vet))
print(round(d,3))