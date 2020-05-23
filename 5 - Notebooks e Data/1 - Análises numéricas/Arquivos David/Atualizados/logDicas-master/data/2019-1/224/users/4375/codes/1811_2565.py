from numpy import*
mf=array(eval(input("media final: ")))
f=array(eval(input("frequencia: ")))
ch=float(input("carga horaria da disciplina:"))
x=zeros(3, dtype=int)
r=ch*75/100 #formula 
for i in range (size(mf)):
	if(mf[i]>=5) and (f[i]>=r):
		x[0]=x[0]+1
	if(mf[i]<5):
		x[1]=x[1]+1
	if(f[i]<r):
		x[2]=x[2]+1
print(x)
		
	
