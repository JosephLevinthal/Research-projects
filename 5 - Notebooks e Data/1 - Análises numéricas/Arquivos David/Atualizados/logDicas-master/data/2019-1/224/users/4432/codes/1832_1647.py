from numpy import*
y=0
x=array(eval(input("frequenciados alunos  ")))
for elemento in x:
	if( elemento >= 70):
		y=y+1
print(y)
for w in x:
	y=0
	if(x[y]>=70):
		y=y+1
m=zeros(y,dtype(int))
print(m)
	
	