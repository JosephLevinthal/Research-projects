from numpy import*
v=array(eval(float("valor dos itens: ")))
i=0
while(v[i]!=80.00):
	if(v[i]>80.00):
		com = sum(v)-sum(v[1])*15/100
	else:
		com = sum(v)
	i=i+1
print(com)
