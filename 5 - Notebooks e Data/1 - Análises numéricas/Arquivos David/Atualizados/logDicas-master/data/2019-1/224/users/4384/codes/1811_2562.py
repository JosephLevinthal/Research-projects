from numpy import*
v=array(eval(input("digite o vetor:")))
while(size(v)>1):
	v=array(eval(input("digite o vetor:")))
	npar=0
	nimpa=size(v)
	for elemento in v:
		if(elemento%2==0):
			npar=npar+1
			nimpa=nimpa-npar
			print(npar)
			print(nimpa)
			print(size(v))
v=array(eval(input("digite o proximo vetor:")))