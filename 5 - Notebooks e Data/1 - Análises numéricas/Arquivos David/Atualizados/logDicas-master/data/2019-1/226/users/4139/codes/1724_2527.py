n = int(input("numero perfeito: "))

i=1
a=0
while(i<n):
	p = n % i
	i = i + 1
	if(p == 0):
		print(i-1)
		a = a + (i-1)
	
	else:
		c = a+i

if(a == n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")