from numpy import*

a = array(eval(input("sorte:")))
b = zeros(36,dtype=int)

for x in range(size(a)):
	if a[x] > 0:
		b[x] = b[x] + 1
	
print(b)