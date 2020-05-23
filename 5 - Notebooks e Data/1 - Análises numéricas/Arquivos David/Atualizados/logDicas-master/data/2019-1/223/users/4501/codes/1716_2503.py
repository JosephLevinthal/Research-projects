num = int(input("numero: "))      
a=0
b=1
c=1
while(c <= num):
	a=a+(-4/b)*((-1)**c)
	b=b+2
	c=c+1
print(round(a, 8))	