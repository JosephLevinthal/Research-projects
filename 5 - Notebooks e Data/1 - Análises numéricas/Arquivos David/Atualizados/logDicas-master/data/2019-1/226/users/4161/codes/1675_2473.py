ano = int(input("ano: "))
a = ano%19
b = ano%4
c = ano%7
d = (19*a +24)%30
e = (2*b + 4*c + 6*d + 5)%7
if (not(1900<=ano<=2099)):
	print("ano invalido")
else:
	if (ano==1954) or (ano ==2049) or (ano ==1981) or (ano == 2076):
		if (22+d+e > 31):
			print(22+d+e - 38, "-", 4, "-", ano)
		else:
			print(22+d+e - 7, "-",3 ,"-",ano)
	elif (22+d+e > 31):
		print(22+d+e - 31, "-", 4, "-", ano)
	else:
		print(22+d+e, "-",3 ,"-",ano)