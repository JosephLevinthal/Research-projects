from numpy import*
n=array(eval(input("Insira as  notas:")))
no=array(eval(input("Insira os nomes:")))

i=0
s1=0
s2=0
s3=0
m=0

while(i<size(n)):
	if(n[i]==-1):
		s1+=1
	if(6<=n[i]<=10):
		s2+=1
		m=m+n[i]
	if(0<=n[i]<6):
		s3+=1
		m=m+n[i]
	if(n[i]==max(n)):
		s5=no[i]
	i=i+1
quantidade=s2+s3
s4=m/quantidade
print(s1)
print(s2)
print(s3)
print(round(s4,2))
print(s5)