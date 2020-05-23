from numpy import*
n = array(eval(input("notas: ")))
a = array(eval(input("alunos: ")))
#n = array(eval(input("notas: ")))
i=0
f=0
ap=0
r=0
soma=0
c=0
med=0
while(i<size(a)):
	if(n[i]==-1):
		f=f+1
		#i=i+1
	elif(n[i]>=6):
		ap=ap+1
		#i=i+1
	elif((n[i]<6)and n[i]!=-1):
		r=r+1
		#i=i+1
	if(n[i]!=-1):
		soma=soma+n[i]
	if(n[i]==max(n)):
		c=i
	i=i+1
med=soma/(size(n)-f)	
print(f)
print(ap)
print(r)
print(round(med,2))
print(a[c])
		