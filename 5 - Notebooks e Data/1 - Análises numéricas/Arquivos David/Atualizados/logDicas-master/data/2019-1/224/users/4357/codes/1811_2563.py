from numpy import*
notas=array(eval(input("digite o numero: ")))
while(size(notas)>1):
	soma=0
	for i in range(size(notas)):
		if(notas[i]>=5 and notas[i]<7):
			soma = soma + 1
	print(soma)
	notas = array(eval(input("Proximo vetor: ")))	