x = float(input("digite um numero:"))
k = int(input("digite um numero inteiro:"))
soma = 2
m = 0
while(x >= -1) and (k > m):
	soma = soma + ((x**3)/3)+((x**5)/5)*(-1)**2
	m = m + 1
print(round(soma, 8))