x = int(input())
y = int(input())

a = x//10
b = x%10
c = y//10
d = y%10
if not(a!= c and a != d and b != c and b!= d):
	if a == c and b == d:
		print("Ganhou R$ 100.000,00")
	else:
		if a == d and b == c:
			print("Ganhou R$ 50.000,00")
		else:
			print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")