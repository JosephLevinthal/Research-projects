tipograu = input("Informe a conversap (C)-Celsius ou (F)-Fahrenheit : ")
valor = float(input("Valor a ser convertido :"))

if(tipograu.upper() == 'F'):
	convertido = (5/9)*(valor-32)
if(tipograu.upper() == 'C'):
	convertido = ((9/5)*valor)+32
print(round(convertido,2))	