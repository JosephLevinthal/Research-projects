medida = input("Digite a medida: (C/F) ")
temp = float(input("Temperatura: "))
tf = (1.8*temp)+32
tc = (temp-32)/1.8
if (medida == "C"):
	print(round(tf,2))
else:
	print(round(tc,2))
