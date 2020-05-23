from numpy import*
p = array(eval(input()))
a = array(eval(input()))
imc = zeros(size(p), dtype=float)
imc = p/a**2
x = 0
for x in range(0,size(imc)):
	imc[x] = round(imc[x],2)
print(imc)
print("O MAIOR IMC DA TURMA EH:",round(max(imc),2))
if(max(imc)<17):
	print("MUITO ABAIXO DO PESO")
elif(17<=max(imc)<18.5):
	print("ABAIXO DO PESO")
elif(18.5<=max(imc)<25):
	print("PESO NORMAL")
elif(25<=max(imc)<30):
	print("ACIMA DO PESO")
elif(30<=max(imc)<35):
	print("OBESIDADE")
elif(35<=max(imc)<40):
	print("OBESIDADE SEVERA")
elif(max(imc)>40):
	print("OBESIDADE MORBIDA")