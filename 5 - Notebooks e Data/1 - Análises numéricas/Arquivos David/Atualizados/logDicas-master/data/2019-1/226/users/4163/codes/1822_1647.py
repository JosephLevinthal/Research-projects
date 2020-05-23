from numpy import*
al= array(eval(input("presen dos alunos: ")))

ap = 0
 
	
for i in range(size(al)):
	if al[i]>=70:
		ap = ap + 1
print(ap)

lis = zeros(ap, dtype=int)
x = 0
for i in range(size(al)):
	if al[i]>=70:
		lis[x] = lis[x] + i
		x = x + 1
print(lis)