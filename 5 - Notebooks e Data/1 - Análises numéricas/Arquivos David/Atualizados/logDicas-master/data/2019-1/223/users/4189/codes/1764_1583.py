x=input("x= ")

i=0
s=""

while(i<len(x)):
	if(len(x)>=3)and(len(x)%3==0):
		d=x[i:i+3]
	if(len(x)-3>i):
		s+=d+"."
	else:
		s+=d
	i+=3
print(s)

