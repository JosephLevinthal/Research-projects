from numpy import*
v=array(eval(input("digite as notas: ")))
n=array(eval(input("digite os nomes ")))
f=0
a=0
r=0
i=0
soma=0

while(i<size(v)):
	if(v[i]==-1):
		f=f+1

	elif(v[i]>=6):
		a=a+1
		
	elif(v[i]<6 and v[i]!=-1):
		r=r+1
	if(v[i]!=-1):
		soma=soma+v[i]
		
	i=i+1
p=0	
while(v[p]!=max(v)):
	p=p+1
print(f)
print(a)
print(r)
print(round(soma/(size(v)-f),2))
print(n[p])
