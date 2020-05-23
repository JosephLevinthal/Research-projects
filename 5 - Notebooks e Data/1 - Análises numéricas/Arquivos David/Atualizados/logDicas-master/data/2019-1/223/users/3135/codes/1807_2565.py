from numpy import*
cont= zeros(3, dtype=int)

vn= array(eval(input("Insira as medias finais de cada aluno:")))
vp= array(eval(input("Insira o numero de horas de cada aluno:")))
ch= float(input("Insira a carga horaria da disciplina:"))
f= ch * 0.75

for i in range(size(vn)) and range(size(vp)):
	if(vn[i]>=5 and vp[i]>=f):
		cont[0]=cont[0]+1
	elif(vn[i]<5 and vp[i]>=f):
		cont[1]= cont[1]+1
	elif(vn[i]>=5 and vp[i]<f):
		cont[2]= cont[2]+1
print(cont)