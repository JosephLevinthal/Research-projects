from numpy import*
p = array(eval(input("peso dos alunos:")))
h = array(eval(input("altura dos alunos:")))
imc = zeros(size(p) , dtype=float)

for i in range(size(p)):
	imc[i] = round((p[i] / (h[i] * h[i])) , 2)
print(imc)
print("O MAIOR IMC DA TURMA EH:" , imc.max())
if(imc.max() <= 17):
	print("MUITO ABAIXO DO PESO")
elif(imc.max() <= 18.49):
	print("ABAIXO DO PESO")
elif(imc.max() <= 24.99):
	print("PESO NORMAL")
elif(imc.max() <= 29.99):
	print("ACIMA DO PESO")
elif(imc.max() <= 34.99):
	print("OBESIDADE")
elif(imc.max() <= 39.99):
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")