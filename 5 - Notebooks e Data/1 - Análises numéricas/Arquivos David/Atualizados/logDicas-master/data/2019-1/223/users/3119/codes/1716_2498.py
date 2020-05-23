a = int(input("Digite o numero de habitantes da cidade A: "))
b = int(input("Digite o numero de habitantes da cidade B: "))
cres_a = float(input("Percentual de crescimento da cidade A: "))
cres_b = float(input("Percentual de crescimento da cidade B: "))

soma = 0
while(a < b and cres_a > cres_b ):
	a = (a * (cres_a/100)) + a
	b = (b * (cres_b/100)) + b
	soma = soma + 1
print(soma)