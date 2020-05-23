from numpy import*
vet = array(eval(input("faltas: ")))
s=0
t=0
q=0
qi=0
se=0
sa=0
for i in range(size(vet)):
	if(vet[i]==2):
		s=s+1
	elif(vet[i]==3):
		t=t+1
	elif(vet[i]==4):
		q=q+1
	elif(vet[i]==5):
		qi=qi+1
	elif(vet[i]==6):
		se = se+1
	elif(vet[i]==7):
		sa= sa+1
j = s+t+q+qi+se+sa
c = zeros(6, dtype=float)
for i in range(size(c)):
	c[0]= round(((s/j)*100),1)
	c[1]= round(((t/j)*100),1)
	c[2]= round(((q/j)*100),1)
	c[3]= round(((qi/j)*100),1)
	c[4]= round(((se/j)*100),1)
	c[5]= round(((sa/j)*100),1)
print(c)

