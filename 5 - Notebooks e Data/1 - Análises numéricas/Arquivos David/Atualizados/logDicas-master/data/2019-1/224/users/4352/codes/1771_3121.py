from numpy import*
e = array(eval(input("digite o vetor 1: ")))
b = array(eval(input("digite o vetor 2: ")))
i=0
s1=0
s2=0
while(i<size(e)):
	if(e[i]==11) and (b[i]==11):
		s1=s1+0
		s2=s2+0
	elif(e[i]==22) and (b[i]==22):
		s1=s1+0
		s2=s2+0
	elif(e[i]==33) and (b[i]==33):
		s1=s1+0
		s2=s2+0
	
	
	elif(e[i]==11) and (b[i]==22):
		s1=s1+0
		s2=s2+1
	elif(e[i]==11) and (b[i]==33):
		s1=s1+1
		s2=s2+0
	elif(e[i]==22) and (b[i]==11):
		s1=s1+1
		s2=s2+0
	elif(e[i]==22) and (b[i]==33):
		s1=s1+0
		s2=s2+1
	elif(e[i]==33) and (b[i]==11):
		s1=s1+0
		s2=s2+1
	elif(e[i]==33) and (b[i]==22):
		s1=s1+1
		s2=s2+0
	i=i+1
print(i)
if(s1>s2):
	print("EUSAPIA")
elif(s1<s2):
	print("BARSANULFO")
elif(s1==s2):
	print("EMPATE")