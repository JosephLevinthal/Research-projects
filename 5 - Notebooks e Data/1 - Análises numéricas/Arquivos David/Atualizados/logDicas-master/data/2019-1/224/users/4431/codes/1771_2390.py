from numpy import*
x=array(eval(input("Digite a quantidade de presentes por mes: ")))
y=array(eval(input("Digite a quantidade de faltantes por mes: ")))
z=0
m=zeros(len(x),dtype=int)

while(len(x)>z):
	m[z]=x[z]-y[z]
	z=z+1
t=0
while(m[t]!=max(m)):	
	t=t+1
print(t+1)	

		
		
		

	
	
		
		