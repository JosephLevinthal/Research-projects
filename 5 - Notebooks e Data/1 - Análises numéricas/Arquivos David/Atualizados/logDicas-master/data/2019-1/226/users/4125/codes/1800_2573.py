from numpy import*
from math import*
x = array(eval(input("digite peso em kg: ")))
y = array(eval(input("digite a altura em m: ")))
for i in range(size(x)):
	x[i] = round((x[i]/(y[i]**2)),2)
	i = i + 1
print(x)
if (max(x)<17):
	msg = "MUITO ABAIXO DO PESO"
elif(17<max(x)<=18.49):
	msg = "ABAIXO DO PESO"
elif(18.5<max(x)<=24.99):
	msg = "PESO NORMAL"
elif(max(x)>25)and(max(x)<=29.99):
	msg = "ACIMA DO PESO"
elif(max(x)>30)and(max(x)<=34.99):
	msg = "OBESIDADE"
elif(max(x)>35)and(max(x)<=39.99):
	msg = "OBESIDADE SEVERA"
elif(max(x)>40):
	msg = "OBESIDADE MORBIDA"
print("O MAIOR IMC DA TURMA EH:",round(max(x),2))
print(msg)