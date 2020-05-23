from numpy import*
n=input("digite o  vetor:")
n=n.upper()
n=n.split(',')
s= zeros(5, dtype=int)
for i in range(size(n)):
	if(n[i]=="AR"):
		s[0]=s[0]+1
	if(n[i]=="BR"):
		s[1]=s[1]+1
	if(n[i]=="CL"):
		s[2]=s[2]+1
	if(n[i]=="CO"):
		s[3]=s[3]+1
	if(n[i]=="UY"):
		s[4]=s[4]+1
print(max(s))
print(s)
