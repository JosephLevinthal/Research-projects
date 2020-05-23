from numpy import*
v =  array(eval(input("Vetor: ")))
i = 0
b = 0
p = 0

while(i < size(v)):
	if(v[i]>99):
		i = i
		p = p + 1
		print(i)
	else:
		p = p + 0
	i = i + 1
print(p)	