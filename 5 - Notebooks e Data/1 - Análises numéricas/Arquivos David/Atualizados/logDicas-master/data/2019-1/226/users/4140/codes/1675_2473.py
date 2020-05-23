ano=int(input())
a=ano%19
b=ano%4
c=ano%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7

if(ano>1900 and ano<2099):
	if(ano!=1954 and ano!=1981 and ano!=2049 and ano!=2076):
		dia=22+d+e
		mes=3
		if(dia>31):
			dia=dia-31
			mes=4
		else:
			dia=dia
			mes=mes
		print(dia,"-",mes,"-",ano)
	else:
		dia=22+d+e
		mes=3
		if(dia>31):
			dia=dia-31-7
			mes=4
		else:
			dia=dia
			mes=mes
		print(dia,"-",mes,"-",ano)
else:
	print("ano invalido")