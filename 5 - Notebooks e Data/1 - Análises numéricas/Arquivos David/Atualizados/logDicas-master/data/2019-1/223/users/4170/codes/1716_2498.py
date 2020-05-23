a = int(input("Numero de habitantes de uma cidade A: "))
b = int(input("Numero de habitantes de uma cidade B: "))
cpa = float(input("Crescimento populacional da cidade A: "))
cpb = float(input("Crescimento populacional da cidade B: "))

soma = 0
while(a < b and cpa > cpb):
	a = (a * (cpa/100)) + a
	b = (b * (cpb/100)) + b
	soma = soma + 1
print(soma)	