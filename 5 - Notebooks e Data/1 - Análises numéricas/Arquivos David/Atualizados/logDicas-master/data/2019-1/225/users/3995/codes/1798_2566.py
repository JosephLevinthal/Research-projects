from numpy import*
f=array(eval(input("faltas:")))
s=0
t=0
q=0
q1=0
se=0
sa=0
for i in range(size(f)):
	if(f[i]==2):
		s+=1
	elif(f[i]==3):
		t+=1
	elif(f[i]==4):
		q+=1
	elif(f[i]==5):
		q1+=1
	elif(f[i]==6):
		se+=1
	elif(f[i]==7):
		sa+=1
h=s+t+q+q1+se+sa
j=zeros(6,dtype=float)
for i in range(size(j)):
	j[0]=round(((s/h)*100),1)
	j[1]=round(((t/h)*100),1)
	j[2]=round(((q/h)*100),1)
	j[3]=round(((q1/h)*100),1)
	j[4]=round(((se/h)*100),1)
	j[5]=round(((sa/h)*100),1)
print(j)