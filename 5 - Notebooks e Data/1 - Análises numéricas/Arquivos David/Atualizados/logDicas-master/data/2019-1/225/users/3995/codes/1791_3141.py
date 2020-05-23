from numpy import*
n=array(eval(input("quantidade:")))

i=0
M=0
while(i<size(n)):
	M=M+(n[i])**(1/6)
	i+=1
print(round(((M/size(n))**6),2))