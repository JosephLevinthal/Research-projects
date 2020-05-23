a = int(input("numero: "))
t = 0
b = 1
d = 0
while (a>0) and (b<a):
	if (a%b == 0):
		print(b)
		d = b + d
		b = b + 1
		t = t + 1
	else:
		b = b + 1
if (d == a):
	print("PERFEITO")
else:
	print("NAO PERFEITO")

