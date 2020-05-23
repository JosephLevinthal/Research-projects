n = int(input("digite o numero: "))
if(n == 1):
	print("1")
	print("PERFEITO")
else:
	i = 0
	b = 1
	e = 0
	s = 0
	while(i<n):
		if(n % b == 0 and n != b):
			s = s + b
			print(b)
			e = e + 1
		b = b + 1
		i = i + 1
	if(s == n):
		print("PERFEITO")
	else:
		print("NAO PERFEITO")