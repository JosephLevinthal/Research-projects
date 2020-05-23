from numpy import *
faltas=array(eval(input('Digite:  ')))
contadora=zeros(6,dtype=float)
for i in faltas:
	if i==2:
		contadora[0]= contadora[0]+1
	elif i==3:
		contadora[1]= contadora[1]+1
	elif i==4:
		contadora[2]=contadora[2]+1	
	elif i==5:	
		contadora[3]= contadora[3]+1
	elif i==6:	
		contadora[4]= contadora[4]+1
	else:
		contadora[5]=contadora[5]+1

for i in range(0,size(contadora),1):
	contadora[i]=round(contadora[i]/size(faltas)*100,1)
	
print(contadora)
