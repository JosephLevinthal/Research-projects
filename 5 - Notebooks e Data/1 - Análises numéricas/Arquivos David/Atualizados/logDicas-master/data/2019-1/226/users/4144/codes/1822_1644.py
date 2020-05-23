from numpy import *
a = array(eval(input("notas: ")))
k = 0
for i in range(size(a)):
	if(a[i]<5):
		k = k + 1
print(k)
s = 0
x = zeros(k, dtype=int)
for i in range(size(a)):
	if(a[i]<5):
		x[s]=i
		s = s + 1
print(x)
		