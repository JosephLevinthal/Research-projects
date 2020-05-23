from numpy import*

vet = array(eval(input("Saques:")))

x = 0

for i in range(size(vet)):
	if(vet[i]<=50):
		x = x + 1
print(x)
a = 0
d = zeros(x, dtype=int)
for i in range(size(vet)):
	if(vet[i]<=50):
		d[a] = i
		a = a + 1
print(d)
	