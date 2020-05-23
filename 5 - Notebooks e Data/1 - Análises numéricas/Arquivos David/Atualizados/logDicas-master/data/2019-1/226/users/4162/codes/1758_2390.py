from numpy import*
i=0
pm=array(eval(input("insira a quantidade de alunos por mes: ")))
fm=array(eval(input("insira a quantidade de alunos faltosos por mes: ")))
rm=pm-fm
while i!=size(pm):
	if rm[i]==max(rm):
		print(i+1)
	i=i+1

