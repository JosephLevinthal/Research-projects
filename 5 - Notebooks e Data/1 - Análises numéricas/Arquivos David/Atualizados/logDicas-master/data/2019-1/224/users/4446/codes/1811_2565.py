from numpy import *
vm=array(eval(input("digite a medias finais dos alunos: ")))
vh= array(eval(input("digite as horas frequentada: ")))
ch=int(input("carga horaria da disciplina: "))
t=zeros(3, dtype=int)
for i,j in zip(vm,vh):
	if (i>= 5) and (j>=ch*(75/100)) :
		t[0]= t[0]+1
	if (i<5):
		t[1]= t[1]+1
	if (j<ch*(75/100)):
		t[2]= t[2]+1
print(t)