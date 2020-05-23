a=float(input("altura    "))
b=input("sexo  M   OU    F   ")
pf=(62.1*a)-44.7
pm=(72.7*a)-58
if(b.upper()=="M"):
	print(round(pm,2))
else:
	if(b.upper()=="F"):
		print(round(pf,2))
	
	