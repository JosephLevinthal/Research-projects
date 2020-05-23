n = int(input("digite o numero inteiro: "))
n1 = int(input("digite o segundo numero inteiro: "))
b = 1
t = 0
d = 0
while(n>0)and(b<n):
	if(n%b==0): 
		d = b + d
		b = b + 1
		t = t + 1
	else:
		b = b + 1

d1 = 0 
t1 = 0
b1 = 1 
while(n1>0)and(b1<n1):
	if(n1%b1==0): 
		d1 = b1 + d1
		b1 = b1 + 1
		t1 = t1 + 1
	else:
		b1 = b1 + 1
print(d)
print(d1)
if(d == n1)and(d1==n):
	print("amigos".upper())
else:
	print("nao amigos".upper())