from numpy import*
n=array(eval(input("vetor de notas dos alunos: ")))
a=0

for v in n:
	if v>=5:
		a= a + 1

ap= zeros(a,dtype=int)
i=0
c=0
for v in n:
	if n[i]>=5:
		ap[c]=i
		c= c + 1
	i= i + 1
print(a)
print(ap)