a=int(input("numeros de habitantes A:"))
b=int(input("numeros de habitantes B:"))
pa=float(input("percentual A:"))
pb=float(input("percentual B:"))
t=0
while(a<b):
	h=(a*pa)/100
	a=a+h
	j=(b*pb)/100
	b=b+j
	t=t+1
	if(a>=b):
		print(t)