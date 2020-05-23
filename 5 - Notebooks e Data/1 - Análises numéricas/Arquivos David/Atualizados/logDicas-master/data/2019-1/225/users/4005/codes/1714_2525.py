x= int(input("numero inteiro:"))
c=1
t=0

while(c<x):
	if(x%c==0):
		t+=1
if(t!=0):
	print(t)