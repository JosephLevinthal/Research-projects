a = int(input("numero de habitantes A: "))
b = int(input("numero de habitantes B: "))
ca = float(input("crescimento de A: "))
cb = float(input("crescimento de B: "))
t = 0
if (a<b) and (ca>cb):
	while (a<=b):
		a = a + ca*a/100
		b = b + cb*b/100
		t = t + 1
print(t)