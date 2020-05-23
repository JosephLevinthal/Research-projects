from numpy import*
n=array(eval(input("notas:")))
l=array(eval(input("nomes:")))

m=0 #faltaram
h=0 #Aprovados
j=0 #Reprovados
p=0 #presentes
i=0 #contador
n1=0 #notas dos aprovados
n2=0 #notas dos reprovados
while(i<size(n)):
	if(n[i]>-1 and n[i]<=10):
		p=p+1
		if(n[i]>=6 and n[i]<=10):
			h=h+1
			n1=n1+n[i]
			
		elif(n[i]>=0 and n[i]<6):
			j=j+1
			n2=n2+n[i]
	elif(n[i]==-1):
		m=m+1
	i=i+1
i=0
while(n[i]!=max(n)):
	i=i+1
print(m)
print(h)
print(j)
print(round(((n1+n2)/p),2))
print(l[i])