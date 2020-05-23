n = int(input("Numero: "))

i = 0
r = 0
while(i < n):
	i = i + 1
	r = r + 1/(i**2)
	print(i,r)

r = 6 * r
print(r)