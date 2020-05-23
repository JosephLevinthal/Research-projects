#Leitura dos dados pessoais:
a = float(input("digite a altura: "))
s = input("digite o sexo (M ou F): ")
ph = (72.7 * a) - 58
pm = (62.1 * a) - 44.7
if(s == "M"):
	print(round(ph, 2))
else:
	print(round(pm, 2))
	