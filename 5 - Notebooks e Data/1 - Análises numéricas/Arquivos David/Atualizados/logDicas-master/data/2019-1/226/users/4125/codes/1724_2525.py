n = int(input("digite o numero inteiro:"))
t = 0
b = 1
while(n>0)and(b<=n):
	if(n%b==0):
		print(b)
		b = b + 1
		t = t + 1
	else:
		b = b + 1
print(t,"divisores")
	