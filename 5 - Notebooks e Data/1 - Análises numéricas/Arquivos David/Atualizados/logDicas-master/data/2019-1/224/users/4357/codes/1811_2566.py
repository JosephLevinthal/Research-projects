from numpy import*
faltas=array(eval(input("digite o numero:")))
seg,ter,qua,qui,sex,sab=0,0,0,0,0,0
for i in faltas:
	if(i==2):
		seg=seg+1
	if(i==3):
		ter=ter+1
	if(i==4):
		qua=qua+1
	if(i==5):
		qui=qui+1
	if(i==6):
		sex=sex+1
	if(i==7):
		sab=sab+1
d=zeros(6,dtype=float)
d[0]=round((seg/size(faltas))*100,1)
d[1]=round((ter/size(faltas))*100,1)
d[2]=round((qua/size(faltas))*100,1)
d[3]=round((qui/size(faltas))*100,1)
d[4]=round((sex/size(faltas))*100,1)
d[5]=round((sab/size(faltas))*100,1)
print(d)