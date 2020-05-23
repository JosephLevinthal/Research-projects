from numpy import*
x=array(eval(input("Digite a quantidade de alunos : ")))
h=0
for i in x:
	if(i%3==0):
		h=h+1
m=zeros(h,dtype=int)
y=0
print(h)
h=0
for i in x:
	if(i%3==0):
		m[y]=h
		y=y+1
		h=h+1
	else:
		h=h+1
print(m)			
		
			
			