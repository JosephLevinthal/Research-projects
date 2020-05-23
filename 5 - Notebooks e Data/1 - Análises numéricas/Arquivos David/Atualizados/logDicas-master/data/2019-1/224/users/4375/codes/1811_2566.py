from numpy import*
flts=array(eval(input("numero de faltas por dia da semana: ")))
x=zeros(6, dtype=int)
for i in range (size(flts)):
	if(flts[i]==2):
		x[0]=x[0]+1
	if(flts[i]==3):
		x[1]=x[1]+1
	if(flts[i]==4):
		x[2]=x[2]+1
	if(flts[i]==5):
		x[3]=x[3]+1
	if(flts[i]==6):
		x[4]=x[4]+1
	if(flts[i]==7):
		x[5]=x[5]+1
xx=zeros(6, dtype=float)
for i in range (size(xx)):
	xx[i]=round((x[i]/(size(flts)))*100,1)
print(xx)

