from numpy import*
mf = array(eval(input("digite as medias finais de cada aluno: ")))
p = array(eval(input("digite a frequencia de cada aluno: ")))
ch = int(input("digite a carga horaria da disciplina: "))
chp = ch*.75
cont = zeros(3, dtype=int)
for i in range(size(mf)):
	if mf[i] >= 5 and p[i] >= chp:
		cont[0] = cont[0] + 1
	elif mf[i] < 5:
		cont[1] = cont[1] + 1
	elif mf[i] >= 5 and p[i] < chp:
		cont[2] = cont[2] + 1
print(cont)