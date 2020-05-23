frase = input("Digite uma palavra ou frase: ") #coleta a palavra de entrada que sera testada

frase = frase.upper() #passa a frase para maiuscula
new = frase.replace(" ","") #elimina os espacos da frase
inv = "" #vetor vazio que recebera a nova string na ordem inversa
i = -1 #incrementa o laco a partir do ultimo valor
while(i >= -len(new)): #O tamanho da string final é negativo, ex -9, assim como comeca em -1, esse valor e maior que a posicai final do vetor
	inv = inv+new[i] #copia a nova letra para dentro do vetor vazio, na posicao i
	i = i-1 #incrementa o laco em mais uma posicao
print(new) #imprime a expressao sem espacos
if(new == inv): #testa se a palavra original eh igual a inversa
	print(1) # se for, imprime 1, isto eh, um palindromo
else: #se nao for
	print(0)	#imprime zero, isto eh, nao eh palindromo
