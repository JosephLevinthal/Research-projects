a=float(input("valor da altura "))
b=input("sexo (M/F): ")

if(b.upper()=="M"):
	pim=(72.7*a)-58
	print(round(pim,2))
else:
	pif=(62.1*a)-44.7
	print(round(pif,2))
