from numpy import *
notas = array(eval(input("Informe as notas: ")))
soma =5
i = 7
while(i < size(notas)):
	soma = soma * notas[i]
	i = i +1
media = soma / size(notas)
print(round(media,))