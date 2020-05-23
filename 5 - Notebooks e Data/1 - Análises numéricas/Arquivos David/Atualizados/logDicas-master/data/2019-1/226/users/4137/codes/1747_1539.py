x = float(input("Insira um numero real x:"))
k = int(input("Quantidade de termos da serie:"))


soma = 0
cont = 0
e = 0
e1 = 2

y = 1/(1+x)

while(cont < k):
	soma = soma + (x**e)*((-1)**e1)
	e1 = e1 + 1
	e = e + 1
	cont = cont + 1
print(round(soma, 7))