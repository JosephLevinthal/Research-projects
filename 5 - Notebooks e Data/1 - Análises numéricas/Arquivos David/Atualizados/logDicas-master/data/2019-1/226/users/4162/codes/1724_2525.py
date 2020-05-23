num= int(input("insira um numero: "))
x=1
t=0
while x<=num:
	y=num%x
	if(y == 0):
		print(x)
		t = t + 1
	x=x+1
if t==0:
	print("1 divisor")
else:
	print(t,"divisores")