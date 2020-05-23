from numpy import*

n=array(eval(input("entre como vetor: ")))
a=array(eval(input("entre como vetornome: ")))

i=0
falt=0
apro=0
rep=0
soma=0
while(i<size(n)):
	if(n[i]==-1):
		falt=falt+1
	elif(n[i]>=6):
		apro=apro+1
	elif(n[i]<6 and n[i]!= -1):
		rep=rep+1
	if(n[i] != -1):
		soma=soma+ n[i]
	if(n[i]==max(n)):
		maior=i
	i=i+1
s=soma/(size(a)-falt)
print(falt)
print(apro)
print(rep)
print(round(s,2))
print(a[maior])

