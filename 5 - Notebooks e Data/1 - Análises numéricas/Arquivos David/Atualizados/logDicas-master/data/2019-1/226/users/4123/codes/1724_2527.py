n = int(input())
i = 1
s = 0

while i<n:
	if n%i == 0:
		print(i)
		s+=i
	i+=1
if s==n:
	print("PERFEITO")
else:
	print("NAO PERFEITO")
	