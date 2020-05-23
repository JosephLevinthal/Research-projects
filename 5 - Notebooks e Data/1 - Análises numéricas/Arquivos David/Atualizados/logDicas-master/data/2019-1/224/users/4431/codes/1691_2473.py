x=int(input("Digite o ano: "))
a=x%19
b=x%4
c=x%7
d=((19*a)+24)%30
e=(2*b+4*c+6*d+5)%7
f=(22+d+e)
if(f>31):
	f=f-31
	u=4
else:
	u=3
if(x<1900)or(x>2099):
	print("ano invalido")
elif(x!=1954)and(x!=1981)and(x!=2049)and(x!=2076):
	print(f,"-",u,"-",x)
else:
	f=f-7
	print(f,"-",u,"-",x)
	