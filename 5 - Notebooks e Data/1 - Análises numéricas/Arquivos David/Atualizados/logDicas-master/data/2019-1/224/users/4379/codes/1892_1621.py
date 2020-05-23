from numpy import*
c=array(eval(input("digite: ")))
q=array(eval(input("digite: ")))
mat=array([1.25,2.6,1.8,0.85,3.2])
s=0
for i in range(len(c)):
	if(c[i]=="ARROZ"):
		s=s+q[i]*mat[0]
	if(c[i]=="FEIJAO"):
		s=s+q[i]*mat[1]
	if(c[i]=="BIS"):
		s=s+q[i]*mat[2]
	if(c[i]=="MIOJO"):
		s=s+q[i]*mat[3]
	if(c[i]=="FANTA"):
		s=s+q[i]*mat[4]
print(round(s,2))