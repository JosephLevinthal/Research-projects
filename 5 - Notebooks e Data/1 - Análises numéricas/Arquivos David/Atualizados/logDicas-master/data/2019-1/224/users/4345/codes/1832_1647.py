from numpy import*
f=array(eval(input("digite a frequencia dos alunos: ")))
ap=0
y=0
for element in f:
	if element >=70:
		ap=ap+1
print(ap)
n=zeros(y, dtype=int)
for i in range(size(f)):
	if i >=70:
		y=y+1
		n=1
print(n)			