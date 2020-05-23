from numpy import * # Atribui valores a um vetor 'v' 
notas = array(eval(input("Informe as notas: "))) # Soma dos valores do vetor. Comeca em ZERO. 
soma = 0 # Calcula a soma 
for i in range(size(notas)):
	soma = soma + notas[i]  
media = soma / size(notas) 
x=0
x=x/(size(notas)-1)
x=x**0.5
print(round(x,3))
	