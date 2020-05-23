from numpy import *
ordem = array(eval(input("Digite uma matriz contendo letras L ou B: ")))
bombas = 0
for i in range(shape(ordem)[0]):
	for j in range(shape(ordem)[1]):
		if(ordem[i,j] == "B"):
			bombas = bombas + 1
print(bombas)			