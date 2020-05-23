from numpy import*
mf = array(eval(input("Medias finais dos alunos: ")))
p = array(eval(input("Presenca dos alunos: ")))
ch = int(input("Carga horaria da disciplina: "))
x = zeros(3, dtype = int)
for i in range(size(mf)):
	if(p[i]/ch >= 0.75):
		if(mf[i] >= 5):
			x[0] = x[0] + 1
		else:
			x[1] = x[1] + 1
	else:
		x[2] = x[2] + 1
print(x)		
		