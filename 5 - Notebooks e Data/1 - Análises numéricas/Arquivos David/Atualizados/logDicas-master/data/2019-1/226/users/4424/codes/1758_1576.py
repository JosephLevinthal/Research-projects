from numpy import*
v1=array(eval(input("x: ")))
v2=array(eval(input("y: ")))			

i=0
soma1=0
soma2=0
			
while(i<size(v2)) and size(v1)==size(v2):
	if(v1[i]==11 and v2[i]==33) or (v1[i]==22 and v2[i]==11) or (v1[i]==33 and v2[i]==22):
		i=i+1
		soma1=soma1+1
	elif(v1[i]==33 and v2[i]==11) or (v1[i]==11 and v2[i]==22) or (v1[i]==22 and v2[i]==33):
		i=i+1
		soma2=soma2+1
	else:
		i=i+1
print(i)
if(soma1>soma2):
	print("EUSAPIA")
elif(soma2>soma1):
	print("BARSANULFO")
else:
	print("EMPATE")