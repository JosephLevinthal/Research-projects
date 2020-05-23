from numpy import*

notas = array(eval(input("Digite as notas:")))
alunos = array(eval(input("Digite o nome:")))

i = 0
faltaram = 0
passaram = 0
reprovaram = 0
soma = 0
maior = 0

while(i<size(notas)):
	if(notas[i] == -1.0):
		faltaram = faltaram + 1	
		print(faltaram)
	elif(notas[i] >= 6.0):
		passaram = passaram + 1
		print(passaram)
	elif(notas[i] < 6.0 and notas[i] != -1):
		reprovaram = reprovaram + 1
		print(reprovaram)
	elif(notas[i] != -1.0):
		soma = soma + notas[i]
		print(round(soma / (size(notas) - faltaram),2))
	elif(notas[i] == max(notas)):
		maior = i
	i =i+1
	   print(alunos[maior])
	

