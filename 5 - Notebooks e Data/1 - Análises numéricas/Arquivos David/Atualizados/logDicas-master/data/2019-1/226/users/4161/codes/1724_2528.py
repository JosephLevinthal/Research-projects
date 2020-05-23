n = -1000.5
v1 = "ARMSTRONG"
v2 = "NAO ARMSTRONG"
while (n>0) or (n == -1000.5):
	n = int(input("numero: "))
	a = 0
	b = n
	t = 0
	d = 0
	while not(0<b<1):
		b = b/10
		a = a + 1
	while (t<a):
		c = n//(10**t) - n//(10**(t+1))*10
		d = d + c**a
		t = t + 1
	if (d == n):
		print("ARMSTRONG")
		n = -1000.5
	else:
		print("NAO ARMSTRONG")
		n = -1000.5

