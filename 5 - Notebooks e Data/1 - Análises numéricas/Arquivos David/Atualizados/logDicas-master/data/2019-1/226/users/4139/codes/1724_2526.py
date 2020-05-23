n1 = int(input("numero: "))
n2 = int(input("numero: "))

i = 1
a = 0
b = 0

while(i < n1):
	a = n1 % i
	i = i + 1
	if(a == 0):
		b = b + (i-1)
	else:
		a = a

k = 1
c = 0
while(k < n2):
	a = n2 % k
	k = k + 1
	if(a == 0):
		c = c + (k - 1)
	else:
		a = a

print(b)
print(c)
if(n1 == c)and(n2 == b):
	print("AMIGOS")
else:
	print("NAO AMIGOS")