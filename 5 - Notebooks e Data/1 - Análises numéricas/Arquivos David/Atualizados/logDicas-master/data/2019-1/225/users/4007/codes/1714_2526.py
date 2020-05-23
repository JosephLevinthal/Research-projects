n = int(input("digite um numero:"))
m = int(input("digite um numero:"))
s = 0
i = 1
while (i < n):
	if (n % i == 0):
		s = s + i
		
	i = i + 1
print(s)
a = 1
b = 0
while (a < m):
	if (m % a == 0):
		b = b + a

	a = a + 1
print(b)


if (s == m) and (b == n):
	print("AMIGOS")
	
else:
	print("NAO AMIGOS")