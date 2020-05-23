from math import *

angulo = eval(input("Insira o angulo: "))
k = int(input("Insira o numero de termos da serie: "))

sen = angulo
cont = 1

while (cont < k):
	sen = sen + (-1)**(cont) * ((angulo**(cont*2+1))) / factorial((cont*2+1))
	cont = cont + 1
print(round(sen,10))

