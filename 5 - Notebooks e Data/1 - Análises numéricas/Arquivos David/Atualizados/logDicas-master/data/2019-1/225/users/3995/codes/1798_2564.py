from numpy import*
vetg=array(eval(input("gols:")))
vetg1=array(eval(input("gols:")))

v=zeros(3, dtype=int)

v1=0
e=0
d=0

for i in range(size(vetg)):
	if(vetg[i]>vetg1[i]):
		v1=v1+1
	elif(vetg[i]==vetg1[i]):
		e=e+1
	elif(vetg[i]<vetg1[i]):
		d=d+1
	
v[0]=v1
v[1]=e
v[2]=d
print(v)

	