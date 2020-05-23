from numpy import*

a = array(eval(input("notas:")))


i = 0
for i in range(size(a)):
	if a[i] < 70:
		i = i +1
	
b = zeros(i,dtype=int)
j  = 0
for i in range(size(a)):
	if a[i] != 0:
		b[j] = i
		j = j + 1
print(b)
print(x)
