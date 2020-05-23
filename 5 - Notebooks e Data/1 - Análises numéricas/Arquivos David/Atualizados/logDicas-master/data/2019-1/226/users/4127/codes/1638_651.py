h= float(input("qual a altura? "))
sexo= input("qual o sexo? ")
m= (72.7*h)-58
f= (62.1*h)-44.7
if (sexo.upper()=="M"):
	print(round(m,2))
if (sexo.upper()=="F"):
	print(round(f,2))