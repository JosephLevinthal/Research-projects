var= input(" C ou F: ")
temp= float(input("valor da temp: "))

cpf = (1.8*temp)+32
fpc = (temp-32)/1.8

if (var== "C"):
	print(cpf)
else:
	print(fpc)