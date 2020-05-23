from numpy import*

p=array(eval(input("")))
al=array(eval(input("")))

imc=p/(al*al)
for i in range(size(imc)):
	imc[i]=round(imc[i],2)
a=0
for i in range(size(p)):
	if max(imc)<7:
		a="MUITO ABAIXO DO PESO"
	if max(imc)> 17 and max(imc)<18.49:
		a="ABAIXO DO PESO"
	if max(imc)> 18.5 and max(imc)<24.99:
		a="PESO NORMAL"
	if max(imc)> 25 and max(imc)<29.99:
		a="ACIMA DO PESO"
	if max(imc)> 30 and max(imc)<34.99:
		a="OBESIDADE"
	if max(imc)> 35 and max(imc)<39.99:
		a="OBESIDADE SEVERA"
	if max(imc)>40:
		a="OBESIDADE MORBIDA"


print(imc)
print("O MAIOR IMC DA TURMA EH:",max(imc))
print(a)
