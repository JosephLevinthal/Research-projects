from numpy import*
x = array(eval(input("Digite o vetor: ")))
soma = 0
j=1
for i in range(size(x)):
	soma = soma + x[i]
media = soma/size(x)
for i in range(size(x)):
	j= j*abs(x[i]-media)
	q= j**(1/size(x))
print(round(q,3))
	