cidadea = int(input("numero de habitantes da cidade A: "))
cidadeb = int(input("numero de habitantes da cidade B: "))
pa = float(input("Percentual de crescimento populacional a: "))
pb = float(input("Percentural de crescimento populcional b: "))

acumA = 0
acumB = 0
x = (pa/100)
y = (pb/100)

ano = 0

while (cidadea < cidadeb):
	cidadea = cidadea + (cidadea * x)
	cidadeb = cidadeb + (cidadeb * y)
	ano = ano+1
print(ano)