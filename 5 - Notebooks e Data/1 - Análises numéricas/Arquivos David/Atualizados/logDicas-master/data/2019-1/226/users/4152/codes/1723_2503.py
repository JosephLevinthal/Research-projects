n = int(input("Digite aqui o valor de n: "))
#Termo = 4 / i
a = 0
s = 2
i = 1
soma = 0
while (a < n):
	soma = soma + (4 / i) * (-1) ** s
	i = i + 2
	s = s + 1
	a = a + 1
print(round(soma, 8))
	