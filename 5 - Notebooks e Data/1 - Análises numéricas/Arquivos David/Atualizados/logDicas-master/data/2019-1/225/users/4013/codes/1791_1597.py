from numpy import*
v = array(eval(input("custo de cada item:")))
i = 0
d = 5 #desconto

while(i < size(v)):
	if(v[i] > 80):
		v[i] = v[i] - d
	else:
		v[i] = v[i]
	i = i + 1
print(round(sum(v), 2))