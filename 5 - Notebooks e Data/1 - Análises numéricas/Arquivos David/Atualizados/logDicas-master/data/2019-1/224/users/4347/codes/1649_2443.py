# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import * #enfim aprendi como importar agora as 17hrs
r = float(input("raio")) #normal
x = float(input("altura")) #normal
opção= int(input("1 ou 2")) #isso ele pediu na questão é só ver as anteriores que dão opção
vAr = (pi*(x**2)*(3*r-x)/3) #valor do volume do ar que é o mesmo da calota voadora haha
Vesf = (4*pi*(r**3)/3) #formula basica de volume da esfera
Vcombus = (Vesf - vAr) #como segue a dica o volume do combustível é a diferença do Vesfera e Volume ar
if (opção == 1): #blá blá
	print( round (vAr,4)) #round é sempre usado no print para arredondar um number de casas em até o num decimais
if (opção == 2): #sim, escrevi a msm coisa que ta escrita na dica do enunciado.
	print(round(Vcombus, 4)) #round dênuevo.
