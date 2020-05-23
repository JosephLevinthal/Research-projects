alt=float(input("digite a altura: "))
sex=input("e benino ou benina?: M/F")
 

if(sex.upper()=="M"):

	print(round((72.7*alt)-58,2))
	
else:
	print(round((62.1*alt)-44.7,2))
	