t=int(input("habitantes:"))
a=int(input("habitantes:"))
pt=float(input("percetual:"))
pa=float(input("percentual:"))
t=0
while(t<a):
	d=(t*pt)/100
	t=t+d
	h=(a*pa)/100
	a=a+h
	t=t+1
	if(t>=a):
	print(t)
	