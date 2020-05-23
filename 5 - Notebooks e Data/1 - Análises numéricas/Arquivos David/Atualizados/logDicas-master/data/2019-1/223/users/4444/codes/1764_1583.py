n=input('digite:  ')
vec=''
i=0
while(i<len(n)):
	x=i
	y=i+3
	vec=vec + n[x:y]+ '.'
	i=i+3
print(vec[0:-1])
