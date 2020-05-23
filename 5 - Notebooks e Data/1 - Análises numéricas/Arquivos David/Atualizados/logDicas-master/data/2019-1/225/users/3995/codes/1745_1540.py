from math import*
x=eval(input("angulo:"))
k=int(input("termos:"))
n=1.0 #primeiro termo
c=1 #acumuladora da quantidade de termos 
i=0 #diferenca de expoentes e sinais 
y=2 #fatorial 
w=0
f=1
while(c<k):
	if(x>=0 and k>0):
		t=((-1)**(i+1))
		h=((x**f)/(factorial(y)))
		j=t*h
	c+=1
	i+=1
	w=w+j
	y+=2
	f+=1
print(round(w+n, 6))