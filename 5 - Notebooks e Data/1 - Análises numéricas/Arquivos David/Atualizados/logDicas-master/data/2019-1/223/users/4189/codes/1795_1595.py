from numpy import * 
v=array(eval(input("vetor:")))
i=0
nota=0
mn=0
while(i<size(v)):
	if(v[i]>=0 and v[i]<=10):
	   nota = nota + v[i]
	if(v[i]==min(v)):
		mn=v[i]
	i = i+1
nf=((nota)-(mn))/((size(v))-1)
print(round(nf,2))