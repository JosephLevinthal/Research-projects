n = int(input())
i = 1
j = 0

while i<=n:
	if n%i == 0:
		print(i)
		j+=1
	i+=1
print(j,"divisores")
	