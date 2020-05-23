from numpy import*
v1= array(eval(input()))
v2= array(eval(input()))
i=0
vv1=0
vv2=0
while(i<size(v1) and i<size(v2)):
	if(v1[i]==11 and v2[i]==22):
		vv2=vv2+1
	if(v1[i]==22 and v2[i]==11):
		vv1=vv1+1
	if(v1[i]==22 and v2[i]==33):
		vv2=vv2+1
	if(v1[i]==33 and v2[i]==22):
		vv1=vv1+1
	if(v1[i]==11 and v2[i]==33):
		vv1=vv1+1
	if(v1[i]==33 and v2[i]==11):
		vv2=vv2+1
	i=i+1
print(size(v1))
if(vv1>vv2):
	print("EUSAPIA")
elif(vv2>vv1):
	print("BARSANULFO")
else:
	print("EMPATE")
	