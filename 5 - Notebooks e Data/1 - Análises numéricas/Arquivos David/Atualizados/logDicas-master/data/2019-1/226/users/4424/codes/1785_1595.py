from numpy import*
n=array(eval(input("x: ")))

i=0
soma=0

while(i<size(n)):
	n=sum(n)/size(n)
	
	soma+=1
	i+=1

print(round(n,2))