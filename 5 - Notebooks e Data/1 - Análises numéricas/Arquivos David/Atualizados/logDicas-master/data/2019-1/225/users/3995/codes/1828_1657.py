from numpy import*
s=(input("siglas:")).split(',')
v=zeros(5, dtype=int)
az=0
ca=0
fl=0
pa=0
wi=0

for i in range(len(s)):
	if(s[i]=="AZ"):
		az+=1
	elif(s[i]=="CA"):
		ca+=1
	elif(s[i]=="FL"):
		fl+=1
	elif(s[i]=="PA"):
		pa+=1
	elif(s[i]=="WI"):
		wi+=1
	
v[0]=az
v[1]=ca
v[2]=fl
v[3]=pa
v[4]=wi
print(max(v))
print(v)