from math import *

angulo = eval(input("Angulo: "))
k = int(input("Quantidade de termos desejada para a serie: "))

sen = angulo
cont = 1

while(cont < k):
	sen = sen + (-1)**cont * ((angulo**(cont*2+1)) / factorial((cont*2+1)))
	cont = cont + 1
	
print(round(sen,10))