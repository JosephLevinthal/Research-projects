n=int(input('digite numeros inteiros:'))
c=0
b=0
par=0
impar=0

while(n!=0):
	if (n%2==0):
		par=par+n
		c=c+1
	else:
		impar=impar+n
		b=b+1
		n=int(input('n:'))
d=par/c
f=impar/b
print(round(d/4))
print(round(f/4))