from numpy import*
x = array(eval(input("vetor: ")))
i =0
n=0
p =0
w=0
while(i<size(x)):
	if(x[i]>0):
		p= p+1
	i = i+1	
k = zeros(p, dtype=int)	
while(n<size(x)):
	if(x[n]>=0):
		k[w]=x[n]
		w = w +1 
	n = n+1
print(k)	