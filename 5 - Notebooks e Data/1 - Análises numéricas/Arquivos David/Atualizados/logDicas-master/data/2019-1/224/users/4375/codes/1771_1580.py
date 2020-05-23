from numpy import *
notas=array(eval(input("digite as notas: ")))
nomes=array(eval(input("digite um numero: ")))
i=0
f=0
a=0
r=0
s=0
soma=0
pe=0
n=0					  
while(i<size(notas)):
	if(notas[i]==-1):
		f=f+1
	if(notas[i]>=6):
		a=a+1
	if(notas[i]<6 and notas[i]!=-1): 
		r=r+1
	if(notas[i]!=-1):
		s=s+notas[i]
		pe=pe+1			  
	if(notas[i]==max(notas)):
		n=nomes[i]
	i=i+1
print(f)
print(a)
print(r)
print(round(s/pe,2))	
print(n)
						  
					  
