ano= int(input("insira o ano: "))
a=ano%19
b=ano%4
c=ano%7
d=((19*a)+24)%30
e=(2*b+4*c+6*d+5)%7
f=(22+d+e)
g=abs(31-f)
g1=abs(31-f+7)
h=abs(f)
h1=h+7
if (ano>=1900)and(ano<=2099):
	if (ano==1954)or(ano==1981)or(ano==2049)or(ano==2076):
		if f>31:
			print(g1,"-",4,"-",ano)
		elif f<=31:
			print(h1,"-",3,"-",ano)
	elif f>31:
		print(g,"-",4,"-",ano)
	elif f<=31:
		print(h,"-",3,"-",ano)
else:
	print("ano invalido")