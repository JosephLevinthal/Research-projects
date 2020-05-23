from numpy import *
string=input("digite: ")
v=string.split(',')
cores=zeros(5,dtype=int)
for i in range(size(v)):
	if(v[i]=="P"):
		cores[0]=cores[0]+1
	if(v[i]=="C"):
		cores[1]=cores[1]+1
	if(v[i]=="M"):
		cores[2]=cores[2]+1
	if(v[i]=="V"):
		cores[3]=cores[3]+1
	if(v[i]=="A"):
		cores[4]=cores
print(max(cores))
print(cores)
		