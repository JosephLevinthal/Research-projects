from numpy import *

#vetor contendo n numeros reais positivos
v = array(eval(input("Insira um vetor: ")))

i = 0
m = 0

while(i < size(v)):
	m = m + v[i]**5
	i = i + 1
media = (m/size(v))**(1/5)
print(round(media, 2))