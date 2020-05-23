from numpy import *
baixaria=array(eval(input("notas: ")))
meliantes=array(eval(input("alunos: ")))
p=0
falta=0
ap=0
rep=0
while (p<size(baixaria)):
	if (baixaria[p]==-1):
		falta=falta+1
print(falta)
	elif (baixaria[p]>6):
		ap=ap+1
print(ap)
	elif (baixaria[p]<6 or baixaria[p]==-1):
		rep=rep+1
print(rep)
	elif (baixaria[p]>-1):
		media=sum(baixaria)/size(meliantes)
	p=p+1
print(round(media,2))
	elif (baixaria[p]!=max(baixaria)):
	p=p+1
print(meliantes[p])
