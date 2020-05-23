from numpy import*
from numpy.linalg import*
n = int(input("matriz: "))
m = zeros((n,n), dtype=int)
i = 0
j = 0
for x in range(n):
	v = ""
	v = v + input("numeros: ")
	a = ""
	for y in v:
		if y != " ":
			a = a + y
			if y == v[-1]:
				a = int(a)
				m[i,j] = a
		elif ((y == " ")):
			a = int(a)
			m[i,j] = a
			j = j + 1
			a = ""
	i = i + 1
	j = 0
dp = 0
for i in range(n):
	for j in range(n):
		if i == j:
			dp = dp + m[i,j]
ds = 0
for j in range(n):
	ds = ds + m[j, n-1-j]
print(dp-ds)