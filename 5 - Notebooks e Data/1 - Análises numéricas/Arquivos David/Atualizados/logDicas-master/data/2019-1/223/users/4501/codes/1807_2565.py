from numpy import*
a=array(eval(input("alunos aprovados: ")))
b=array(eval(input("reprovados nota: ")))
c=int(input("reprovados frequencia: "))
d=zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>=5 and b[i]>=0.75*c):
		d[0]=d[0]+1
	if(a[i]<=5 and b[i]>=0.75*c):
		d[1]=d[1]+1
	if(a[i]>5 and b[i]<0.75*c):
		d[2]=d[2]+1
print(d)		
	
		