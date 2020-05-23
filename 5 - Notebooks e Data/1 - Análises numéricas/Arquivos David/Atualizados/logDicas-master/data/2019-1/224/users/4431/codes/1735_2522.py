x = int(input("entrada:"))
n=x
y=(n*2)+1
b=1.5
z=0
if n != 1:
	while(n>=1):
		z=((n/y)*b)+1
		b=z
		n=n-1
		y=y-2
	print(round(2*z,10))	
else:
	print("3.0")

