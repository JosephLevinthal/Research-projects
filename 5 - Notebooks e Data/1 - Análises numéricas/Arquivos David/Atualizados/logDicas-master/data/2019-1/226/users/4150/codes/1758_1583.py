from numpy import*
a = input("numero: ")
n = a[0:3]
j = 3
i = 3
k = 6
while(j<len(a)):
	n += "."+a[i:k]
	i+=3
	k+=3
	j+=3
print(n)