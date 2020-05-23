from numpy import * 
a = array(eval(input("vetor: ")))
b = 0
k = 0
while (b < size(a)):
	if (a[b] > 99):
		b = b
		print(b)
		k = k + 1
	b = b + 1
print(k)
		
	