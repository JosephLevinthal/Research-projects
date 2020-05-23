a = int(input("numero1: "))
a1 = int(input("numero2: "))
t = 0
b = 1
d = 0
while (a>0) and (b<a):
	if (a%b == 0):
		d = b + d
		b = b + 1
		t = t + 1
	else:
		b = b + 1
t1 = 0
b1 = 1
d1 = 0
while (a1>0) and (b1<a1):
	if (a1%b1 == 0):
		d1 = b1 + d1
		b1 = b1 + 1
		t1 = t1 + 1
	else:
		b1 = b1 + 1
print(d)
print(d1)
if (d1 == a) and (d == a1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")