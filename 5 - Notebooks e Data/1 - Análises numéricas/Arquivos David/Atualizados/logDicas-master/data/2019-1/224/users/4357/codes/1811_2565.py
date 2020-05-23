from numpy import*
media=array(eval(input("digite o numero:")))
presenca=array(eval(input("digite o numero:")))
carhoraria=int(input("digite o numero:"))
a=0
b=0
c=0
for i,j in zip(media,presenca):
	if(i>=5 and j>=carhoraria*(75/100)):
		a=a+1
	if(i<5):
		b=b+1
	if(j<carhoraria*(75/100)):
		c=c+1
d=zeros(3,dtype=int)
d[0]=a
d[1]=b
d[2]=c
print(d)
		
