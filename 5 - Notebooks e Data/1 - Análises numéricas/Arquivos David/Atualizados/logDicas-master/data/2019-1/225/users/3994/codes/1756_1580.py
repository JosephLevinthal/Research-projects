from numpy import*
n= array(eval(input("Digite as notas: ")))
o= array(eval(input("Digite os nomes: ")))
a=0 #faltas
b=0 #aprovados
c=0 #reprovados
d=0 #presentes
i=0 #contador
n1=0 #notas aprovados
n2=0 #notas reprovados

while(i<size(n)):
	if(n[i]>-1 and n[i]<=10):
		d=d+1
		if(n[i]>=6 and n[i]<=10):
			b=b+1
			n1= n1+n[i]
		elif(n[i]>=0 and n[i]<=6):
			c=c+1
			n2=n2+n[i]
	elif(n[i]==-1):
		a=a+1
	i=i+1
i=0
while(n[i]!=max(n)):
	i=i+1
print(a)
print(b)
print(c)
print(round(((n1+n2)/d),2))
print(o[i])


			

