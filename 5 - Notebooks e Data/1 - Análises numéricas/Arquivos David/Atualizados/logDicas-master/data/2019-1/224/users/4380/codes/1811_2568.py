a=int(input("base: "))
t=0
x=a
while(t<a):
	v=x*"*"+2*t*"o"+x*"*"
	x=x-1
	print(v)
	t=t+1