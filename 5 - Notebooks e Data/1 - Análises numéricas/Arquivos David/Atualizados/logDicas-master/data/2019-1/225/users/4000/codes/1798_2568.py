n = int(input(": "))
for i in range(n,0,-1):
	s= i*"*"+2*(n-i)*"o"+i*"*"
	print(s)