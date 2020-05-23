from numpy import*
x=array(eval(input("Digite os coeficientes: ")))
z=-4
r=3
i=-1
h=3
f=" + "
if(len(x)>=3):
	b=str(x[-3])+"x^2"+f+str(x[-2])+"x"+f+str(x[-1])
while(len(x)>h):
	t="x^"+str(r)
	u=str(x[z])+t+f
	b=u+b
	h=h+1
	z=z-1
	r=r+1

if(len(x)==1):
	print(x[0])
elif(len(x)==2):
	print(str(x[-2])+"x"+f+str(x[-1]))
elif(len(x)==3):
	print(b)
else:	
   print(b)	
	


	

	

	

	

