from numpy import*
x=array(eval(input("Digite um vetor: ")))
t=0
while(len(x)>t):
	if(x[t]%2!=0):
		x[t]=x[t]-x[t]
		t=t+1
	else:
		t=t+1
print(x)		
		