e = int(input("qtd estrela: "))
c = e

while(c > 0):
	s = ""
	for i in range (c):
		s = s + "*"
	c = c - 1
	print(s)
c=1
while(c <= e):
	a = ""
	for i in range(c):
		a = a + "*"
	c = c + 1
	print(a)