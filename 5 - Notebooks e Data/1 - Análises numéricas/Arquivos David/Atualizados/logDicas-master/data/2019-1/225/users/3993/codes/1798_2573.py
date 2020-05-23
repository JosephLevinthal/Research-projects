from numpy import*
import numpy as np
v1 = array(eval(input(" ")))
v2 = array(eval(input(" ")))
a=[]
for i in range(len(v1)):
	a.append(round(v1[i]/(v2[i]**2),2))
maior = a[0]
for i in a:
	if maior < i:
		maior  =  i
print(str(a).replace(",",''))
print("O MAIOR IMC DA TURMA EH:",maior)
if maior <= 17:
	print("MUITO ABAIXO DO PESO")
elif maior <= 18.49:
	print("ABAIXO DO PESO")
elif maior <= 24.99:
	print("PESO NORMAL")
elif maior <= 29.99:
	print("ACIMA DO PESO")
elif maior <34.99:
	print("OBESIDADE")
elif maior <= 39.99:
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")