from numpy import*
v = array(eval(input("vetor de notas: ")))
i = 0
while(i<size(v)):
	v[i]=v[i]*(i+1)
	i = i + 1
c = arange(size(v))+1
print(round(sum(v)/sum(c), 2))
