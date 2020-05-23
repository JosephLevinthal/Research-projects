from numpy import*
a = array(eval(input()))
b = zeros(size(a), dtype=int)
d = 0 
for i in range(size(a)):
	if a[i] >= 2000:
		d += 1
print(d)
print(b)