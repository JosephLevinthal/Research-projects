from numpy import *
notas = array(eval(input("Digite as notas dos alunos: ")))
media = mean(notas[:,1])
print(round(media, 2))