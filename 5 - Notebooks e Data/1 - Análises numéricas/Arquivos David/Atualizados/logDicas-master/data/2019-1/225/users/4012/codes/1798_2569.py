from numpy import*
from math import sqrt
x1 = [10,20,30,40,50,60,70,80,90,100]
x = array(eval(input()))

media=0
for i in x:
	media += i

media = media/(size(x))

desvio=0
for i in x:
	desvio += (i-media)**2

desvio = desvio/((size(x))-1)
desvio = round(sqrt(desvio),3)

print(desvio)
