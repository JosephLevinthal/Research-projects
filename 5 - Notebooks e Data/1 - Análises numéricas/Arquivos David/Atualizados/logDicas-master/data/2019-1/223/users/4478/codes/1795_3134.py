from numpy import*
vetor = array(eval(input("numeros: ")))
i = 0 
n = 3
soma = 0
while(i<size(vetor)):
	m = vetor[i]
	v = m**2
	soma = soma + v
	resultado = ((soma*2)/n)**1/2
	i = i + 1
	n = n +1
	soma = soma + 1
print(round(resultado, n)