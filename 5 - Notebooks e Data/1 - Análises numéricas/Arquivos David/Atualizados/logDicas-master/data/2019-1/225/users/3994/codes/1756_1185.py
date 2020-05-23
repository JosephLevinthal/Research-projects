from numpy import*
v= array(eval(input("Digite a glicose: ")))
i=0
j=0
while(i<size(v)):
	if(v[i]>99):
		j= j+1
		print(i)
	else:
		j=j+0
	i=i+1
print(j)
