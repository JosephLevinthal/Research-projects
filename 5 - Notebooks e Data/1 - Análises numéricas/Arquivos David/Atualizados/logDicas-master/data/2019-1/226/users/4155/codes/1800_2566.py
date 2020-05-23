from numpy import*
v = array(eval(input("v: ")))

vet = zeros(6,)

for i in range(size(v)):
	if v[i] == 2:
		vet[0] = vet[0] + 1
	elif v[i] == 3:
		vet[1] = vet[1] + 1
	elif v[i] == 4:
		vet[2] = vet[2] +1
	elif v[i] == 5:
		vet[3] = vet[3] + 1
	elif v[i] == 6:
		vet[4] = vet[4] + 1
	elif v[i] == 7:
		vet[5] = vet[5] + 1	
for i in range(0, size(vet)):
	vet[i] = round(vet[i]/size(v) * 100, 1)
print(vet)
		
			
		
		
	
