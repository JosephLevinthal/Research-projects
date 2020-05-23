from numpy import*

a=array(eval(input('medias finais: ')))
b=array(eval(input('presenca dos alunos na diciplina: ')))
c=int(input('carga horaria da diciplina: '))
d=zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>=5 and b[i]>=0.75*c):
		d[0]=d[0]+1
	elif(a[i]<5 and b[i]>=0.75*c):
		d[1]=d[1]+1
	else:
		d[2]=d[2]+1
print(d)
	