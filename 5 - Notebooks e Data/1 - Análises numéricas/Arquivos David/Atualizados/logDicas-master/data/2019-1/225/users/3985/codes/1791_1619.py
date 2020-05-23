from numpy import*
t= array(eval(input()))
m= array(eval(input()))
i=0
j=0
q=0.005*90
mo=0.005*45
while(i<size(t)):
	if(m[i]=="QUENTE"):
		j= j+(t[i]*q)
	if(m[i]=="MORNO"):
		j= j+(t[i]*mo)
	elif(m[i]=="FRIO"):
		j= j+(t[i]*0)
	i=i+1
print(round(j,2))