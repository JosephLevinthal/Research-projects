from numpy import*

tur = array(eval(input("numero de matricula: ")))
a = 0
b = 0


for i in range(size(tur)):
	if tur[i] % 2 != 0: 
		a = a + 1
	
c = zeros(a, dtype=int)
for i in range(size(tur)):
	if tur[i]%2 != 0:
		c[b] = tur[i]
		b = b +1
print(c)