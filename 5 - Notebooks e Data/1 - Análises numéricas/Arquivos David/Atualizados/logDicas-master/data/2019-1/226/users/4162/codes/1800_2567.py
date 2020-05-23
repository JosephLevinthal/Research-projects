from numpy import*
n=int(input("tamanho: "))
z=zeros(n, dtype=int)
s="*"
for i in range(size(z)):
	s = "*"
	s = "*"*n
	n = n - 1
	print(s)
for i in range(size(z)+1):
	s = "*"
	s = "*"*n
	n = n + 1
	print(s)