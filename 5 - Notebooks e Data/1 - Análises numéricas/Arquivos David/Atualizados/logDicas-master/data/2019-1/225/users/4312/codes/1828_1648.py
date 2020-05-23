from numpy import*
aulas = array(eval(input("Aulas frequentadas: ")))
x = 0
for i in range(0, size(aulas)):
	if(aulas[i]< 70):
		x = x + 1

vet = zeros(x, dtype=int)

for i in range(0, size(vet)):
	y = 0
	if(aulas[i]< 70):
		y = vet[i] + aulas[i] 
		

print(x)
print(vet)
		