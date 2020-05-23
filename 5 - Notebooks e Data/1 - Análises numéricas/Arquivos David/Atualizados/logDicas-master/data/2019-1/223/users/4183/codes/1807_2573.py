from numpy import *
v1 = array(eval(input("Insira o peso: ")))
v2 = array(eval(input("Insira a altura: ")))
vf = array(zeros(3,dtype=float))
imc = 0
msg = 'OI'
for i in range(size(v1)):
	imc = round(v1[i] / (v2[i] * v2[i]),2)
	vf[i] = imc
	if (max(vf) > 40):
		msg = "OBESIDADE MORBIDA"
	elif (39,99 >= max(vf) and max(vf) >= 35):
		msg = "OBESIDADE SEVERA"
	elif (34,99 >= max(vf) and  max(vf) >= 30):
		msg = "OBESIDADE"
	elif (29,99 >= max(vf) and max(vf) >= 25):
		msg = "ACIMA DO PESO"
	elif (24,99 >= max(vf) and max(vf) and max(vf) >= 18,5):
		msg = "PESO NORMAL"
	elif (18,49 >= max(vf) and max(vf) >= 17):
		msg = "ABAIXO DO PESO"
	elif (max(vf) < 17):
		msg = "MUITO ABAIXO DO PESO"
print(vf)
print("O MAIOR IMC DA TURMA EH:", max(vf))
print(msg)

	
	
	
