n = int(input("Numero de vezes:"))

cont = 0 #contador#
m = 0 #termo que vai fazer o quociente aumentar#
e = 2 #expoente pra trocar o sinal da função#
soma = 0

while(cont < n):
	soma = soma + (4/(1+2*m)) * ((-1)**e)
	m = m + 1
	e = e + 1
	cont = cont + 1
print(round(soma, 8))