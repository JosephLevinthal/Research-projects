from numpy import *
saque = array(eval(input("Valores dos saques: ")))
c = 0
for x in saque:
	if (x <= 50):
		c = c + 1
		
print(c)

vet = zeros(c, dtype=int)
x = 0
y = 0 
for i in range(size(saque)):
	if(saque[i] <= 50):
		x = i
		vet[y] = vet[y] + x
		y = y + 1

print(vet)
		