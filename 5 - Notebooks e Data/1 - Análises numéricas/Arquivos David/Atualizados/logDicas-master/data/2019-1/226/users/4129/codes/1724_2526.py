n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

a = 1
b = 1
s = 0
r = 0
while(a < n1):
	rest = n1%a
	if(rest == 0):
		s = a + s
	a = a + 1

while(b < n2):
	res = n2%b
	if(res == 0):
		r = b + r
	b = b + 1
	
print(s)
print(r)

if(s == n2 and r == n1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")