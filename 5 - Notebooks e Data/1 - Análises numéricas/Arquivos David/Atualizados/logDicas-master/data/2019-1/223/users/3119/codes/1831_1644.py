from numpy import*

n = array(eval(input("Digite os valores ")))
p = 0

for i in range(size(n)):
	if(n[i] < 5.0):
		p = p + 1

a = zeros(p, dtype = int)		

i = -1
j = 0

for i in range(size(n)):
	if(n[i] < 5):
		a[j] = i
		j = j + 1
		i = i + 1
		
	
print(p)		
print(a)