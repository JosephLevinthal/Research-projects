from numpy import*
v=array(eval(input("Digite o vetor faltas: ")))

c=zeros(6, dtype=float)
seg=0
ter=0
qua=0
qui=0
sex=0
sab=0

for i in range(size(v)):
	if(v[i]==2):
		seg=seg+1
	elif(v[i]==3):
		ter=ter+1
	elif(v[i]==4):
		qua=qua+1
	elif(v[i]==5):
		qui=qui+1
	elif(v[i]==6):
		sex=sex+1
	elif(v[i]==7):
		sab=sab+1
		
c[0]=round(seg/size(v)*100,1)
c[1]=round(ter/size(v)*100,1)
c[2]=round(qua/size(v)*100,1)
c[3]=round(qui/size(v)*100,1)
c[4]=round(sex/size(v)*100,1)
c[5]=round(sab/size(v)*100,1)
			  
print(c)
			  
			  