n=int(input("Informe o valor de aproximacoes: "))

i=0
pi=0

while (i< n):
	pi = pi + (4/(2*i+1))*(-1)**i
	i=i+1
print (round(pi,8))


	