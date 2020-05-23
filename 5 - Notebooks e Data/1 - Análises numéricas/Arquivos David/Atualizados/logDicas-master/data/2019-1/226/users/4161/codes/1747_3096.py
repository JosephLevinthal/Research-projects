n = int(input("posicao: "))
s = 0
while n!=0:
	if n < 0:
		a = 0
	elif n > 0:
		if n == 1:
			a = 20
		elif n == 2:
			a = 15
		elif n == 3:
			a = 10
		elif (4<=n) and (n<=10):
			a = 11 - n
		elif n>10:
			a = 0
	s = s + a
	n = int(input("posicao: "))
print(s)
			