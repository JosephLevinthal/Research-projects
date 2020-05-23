from numpy import*
v= array(eval(input("Insira a forca do aluno")))
c=0
a=0
for i in range(size(v)):
	if(v[i]%2 == 0):
		c+=1
		cont= zeros(c, dtype=int)
for i in range(size(v)):
	if(v[i]%2 ==0):
		cont[a]=v[i]
		a+=1
print(cont)