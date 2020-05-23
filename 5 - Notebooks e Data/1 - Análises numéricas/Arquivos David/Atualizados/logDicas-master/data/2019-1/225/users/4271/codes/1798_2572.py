from numpy import * 
vet = array(eval(input("Matriculas: ")))
vcont = zeros(2, dtype=int)
for i in range(0, size(vet)):
	if (vet[i] % 2 == 0):
		vcont[0] = vcont[0] + 1
		print("grupo 1")
	else:
		vcont[1] = vcont[1] + 1
		print("grupo 2")
print(vcont)