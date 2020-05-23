from numpy import*
p=array(eval(input("digite as presencas:")))
f=array(eval(input("digite as faltas:")))
pf=p-f
i=0
while(i<size(pf)):
	if(pf[i]==max(pf)):
		print(i+1)
	i=i+1