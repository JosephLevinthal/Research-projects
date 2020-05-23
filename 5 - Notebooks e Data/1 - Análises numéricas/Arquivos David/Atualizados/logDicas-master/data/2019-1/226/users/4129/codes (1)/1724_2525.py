n = int(input("Numero: "))
a = 1
t = 0

while(a <= n):
	b = n%a
	if(b == 0):
		print(a)
		t = t + 1
	a = a + 1
	
if(t == 1):
	print(t,'divisor')
elif(t > 1):
	print(t,"divisores")
