from numpy import*

vet = array(eval(input("Digite: ")))
z = zeros(size(vet), dtype=int)

for i in range(0, size(vet)):
	while(vet[i] == 0):
		vet[i] = vet[-i]
		vet = z
		print(z)
	 
	
	