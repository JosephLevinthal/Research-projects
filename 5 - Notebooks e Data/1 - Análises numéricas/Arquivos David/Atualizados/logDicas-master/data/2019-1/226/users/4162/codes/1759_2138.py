from numpy import*
s=input("digite uma string: ").lower()

a=""
c=s.replace(" ","")
i=0
j=1
while i!=len(c):
	b=c[i:j]
	
	a=a+b
	i=i+1
	j=j+1
print(a)