from numpy import*
v=array(eval(input("x: ")))*1.0
n=array(eval(input("y: ")))

i=0
f=0
aprov=0
reprov=0
soma=0

while(i<size(v)):
	if(v[i]==-1.0):
		f=f+1
	if(v[i]>=6):
		aprov=aprov+1
		soma+=v[i]
	if(v[i]<6.0 and v[i]!=-1.0):
		reprov=reprov+1
		soma+=v[i]
	if(v[i]==max(v)):
		nome=n[i]
	i=i+1
print(f)
print(aprov)
print(reprov)
print(round(soma/(aprov+reprov), 2))
print(nome)