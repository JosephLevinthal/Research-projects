from numpy import*
n=input("digite o vetor: ").split(',')
s= zeros(5, dtype=int)
for i in range(size(n)):
	if(n[i]==("ar").upper()):
		s[0]=s[0]+1
	if(n[i]==("br").upper()):
		s[1]=s[1]+1
	if(n[i]==("cl").upper()):
		s[2]=s[2]+1
	if(n[i]==("co").upper()):
		s[3]=s[3]+1
	if(n[i]==("uy").upper()):
		s[4]=s[4]+1
print(max(s))
print(s)