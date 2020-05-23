from numpy import*
p = array(eval(input("peso dos alunos: ")))
a = array(eval(input("altura dos alunos: ")))
t = zeros(size(p), dtype=float)
h = 0
for i in range (size(p)):
	imc = round((p[i] / (a[i]**2 )), 2)
	t[i] = imc
	h= h + 1
print(t)
print("O MAIOR IMC DA TURMA EH:",max(t))
if(max(t) < 17):
	print("MUITO ABAIXO DO PESO")
elif(max(t) > 17 and max(t) < 18.49):
	print("ABAIXO DO PESO")
elif(max(t) > 18.5 and max(t) < 24.99):
	print("PESO NORMAL")
elif(max(t) > 25 and max(t) < 29.99):
	print("ACIMA DO PESO")
elif(max(t) > 30 and max(t) < 34.99):
	print("OBESIDADE")
elif(max(t) > 35 and max(t) < 39.99):
	print("OBESIDADE SEVERA")
elif(max(t) > 40):
	print("OBESIDADE MORBIDA")

