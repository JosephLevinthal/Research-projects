from numpy import*
i=0
a = array(eval(input("insira a quantidade de alunos por mes: ")))
fm=array(eval(input("insira a quantidade de alunos faltosos por mes: ")))
rm=a-fm
while i!=size(a):
	if rm[i]==max(rm):
		print(i+1)
	i=i+1