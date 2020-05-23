from numpy import *
v = array(eval(input("Digite: ")))
v2 = array(eval(input("Digite: ")))
v3 = zeros(size(v),dtype=float)
imc=0
for i in range(size(v)):
	imc = round(v[i]/v2[i]**2,2)
	v3[i]=imc
	imc=0
print(v3)
print("O MAIOR IMC DA TURMA EH: ",max(v3))
if (max(v3)<=17):
	print("MUITO ABAIXO DO PESO")
elif (max(v3)>17 and max(v3)<=18.49):
	print("ABAIXO DO PESO")
elif(max(v3)>18.5 and max(v3)<=24.99):
	print("PESO NORMAL")
elif(max(v3)>25 and max(v3)<=29.99):
	print("ACIMA DO PESO")
elif(max(v3)>30 and max(v3)<=34.99):
	print("OBESIDADE")
elif(max(v3)>35 and max(v3)<=39.99):
	print("OBESIDADE SEVERA")
elif( max(v3)>40):
	print("OBESIDADE MORBIDA")


