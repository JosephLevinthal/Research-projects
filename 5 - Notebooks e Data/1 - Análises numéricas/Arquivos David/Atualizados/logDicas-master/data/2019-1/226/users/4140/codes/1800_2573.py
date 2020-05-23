from numpy import*
v1=array(eval(input()))
v2=array(eval(input()))
v3=zeros(size(v1))
for i in range(size(v1)):
	imc=v1[i]/(v2[i]*v2[i])
	imc=round(imc,2)
	v3[i]=imc
print(v3)
a=round(max(v3),2)
print("O MAIOR IMC DA TURMA EH:",a)
if (a<17):
	print("MUITO ABAIXO DO PESO")
elif(a>=17 and a<=18.49):
	print("ABAIXO DO PESO")
elif(a>=18.5 and a<=24.99):
	print("PESO NORMAL")
elif(a>=25 and a<=29.99):
	print("ACIMA DO PESO")
elif(a>=30 and a<=34.99):
	print("OBESIDADE")
elif(a>=35 and a<=39.99):
	print("OBESIDADE SEVERA ")
else:
	print("OBESIDADE MORBIDA")