n = int(input("digite um numero: "))
i = 1
s = 0
while (i < n):
	if (n % i == 0):
		s = i + s
		print(i)
	
	i = i + 1
if (s == n):
	print("PERFEITO")
	
else:
	print("NAO PERFEITO")
		