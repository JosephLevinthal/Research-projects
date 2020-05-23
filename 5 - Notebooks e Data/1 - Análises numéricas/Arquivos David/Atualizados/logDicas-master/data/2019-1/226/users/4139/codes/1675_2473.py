ano = int(input("ano: "))

a = ano % 19
b = ano % 4
c = ano % 7
d = ((19 * a)+ 24)% 30
e = ((2 * b)+(4 * c)+(6 * d) + 5)% 7

if(ano>1900)and(ano<2099):
	if(ano == 1954)or(ano == 1981)or(ano == 2049)or(ano == 2076):
		if(d + e >= 17):
			x = (15 + d + e)% 31
			print(x,"-",4,"-",ano)
		else:
			x = 15 + d + e
			print(x,"-",3,"-",ano)
		print(p)
	else:
		if(d + e >= 10):
			x = (22 + d + e)%31
			print(x,"-",4,"-",ano)
		else:
			x = 22 + d + e
			print(x,"-",3,"-",ano)
else:
	print("ano invalido")