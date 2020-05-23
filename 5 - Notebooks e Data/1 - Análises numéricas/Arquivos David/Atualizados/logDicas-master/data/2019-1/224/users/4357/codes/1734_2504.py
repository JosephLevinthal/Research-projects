qinicialvir=int(input("digite o numero:"))
qinicialleu=int(input("digite o numero:"))
pvir=float(input("digite o numero:"))
pleu=float(input("digite o numero:"))
pvir,pleu=pvir/100,pleu/100
dia=0
while(2*qinicialvir>qinicialleu):
	qinicialvir=qinicialvir+qinicialvir*pvir
	qinicialleu=qinicialleu+qinicialleu*pleu
	dia=dia+1
print(dia)
