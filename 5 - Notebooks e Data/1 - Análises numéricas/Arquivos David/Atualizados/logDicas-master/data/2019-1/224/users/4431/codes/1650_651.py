h=float(input("Digite a altura em metros: "))
s=input("Digite F ou M:")
if(s.upper()=="M"):
	m=(72.7*h)-58
	print(round(m,2))
else:
	f=(62.1*h)-44.7
	print(round(f,2))	
	