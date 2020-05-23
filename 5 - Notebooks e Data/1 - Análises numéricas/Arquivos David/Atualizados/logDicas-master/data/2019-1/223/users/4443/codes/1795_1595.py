from numpy import *
notas = array(eval(input("Digite as notas dos trabalhos: ")))
#soma de todas as notas
soma = sum(notas)
minima = min(notas)
validas = soma-minima #subtrai do total a menor nota
total = size(notas)-1 #contador do total de notas
media = validas/total #avalia a media
print(round(media, 2))

