a=int(input("Digite os habitantes de A: "))
b=int(input("Digite os habitantes de B: "))
pa=float(input("Digite o percentual de A: "))
pb=float(input("Digite o percentual de B: "))
t=0
while(a<b):
	d=(a*pa)/100
	a=a+d
	g=(b*pb)/100
	b=b+g
	t=t+1
	if(a>=b):
		print(t)
	