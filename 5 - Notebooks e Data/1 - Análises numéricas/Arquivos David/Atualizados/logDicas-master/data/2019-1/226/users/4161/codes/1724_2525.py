a = int(input("numero: "))
t = 0
b = 1
while (a>0) and (b<=a):
	if (a%b == 0):
		print(b)
		b = b + 1
		t = t + 1
	else:
		b = b + 1
print (t, "divisores")
		