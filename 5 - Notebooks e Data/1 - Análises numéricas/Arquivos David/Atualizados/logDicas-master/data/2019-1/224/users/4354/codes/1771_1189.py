from numpy import *
pal = input("digite a frase: ")
copy = ""
i = 0
#retira os espaços da frase
while(i<len(pal)):
	if(pal[i] == " "):
		copy = copy + ""
	else:
		copy = copy + str(pal[i])
	i = i + 1
print(copy.upper())
valor = 0
i2 = 0
#analisa se a frase é um palindromo ou não
while(i2<len(copy)):
	if(copy[i2] == copy[-1*(i2+1)]): #quando é palindromo então ex: string[0] == string[-1];
		valor = valor + 1             #string[1] == string[-2], e assim por diante.
	else:
		valor = valor + 0
	i2 = i2 + 1
#se o toda a string copy ter simetria, então o valor vai ser igual ao tamanho da string sem espaço.
#pois para todo o copy[i2] == copy[-(1+i2)] no laço, adiciona-se o valor 1, assim para todos os caracteres. 
#se todos os caracteres forem simétricos então o adicionar-se-à 1 a todos os caracteres comparados, o valor chegará ao máximo.
if(valor == len(copy)):
	print("1")
else:
	print("0")
#autor: Lincoln Junior (UFAM)