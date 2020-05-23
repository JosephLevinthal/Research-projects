from numpy import*

num=input("entreo com o numero:")

i=0
k=3
s=""
while(i<len(num)):
	if(i==(len(num)-3)):
		s=s+num[i:k]
		i=i+3
		k=k+3
	else:
		s=s+num[i:k]+"."
		i=i+3
		k=k+3
print(s)
	