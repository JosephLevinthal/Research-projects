from numpy import*
x=array(eval(input("Jogadas de Eusapia: ")))
y=array(eval(input("Jogadas de Barsanulfo: ")))
print(size(x))
f=0
g=0
h=0
o=0
k=0
while(g<(size(x))):
	if((x[f])==(y[f])):
		h=h+1
		g=g+1
		f=f+1
	elif((x[f]==11)and(y[f]==33))or((x[f]==22)and(y[f]==11))or((x[f]==33)and(y[f]==22)):
		o=o+1
		f=f+1
		g=g+1
	elif((y[f]==11)and(x[f]==33))or((y[f]==22)and(x[f]==11))or((y[f]==33)and(x[f]==22)):
		k=k+1
		f=f+1
		g=g+1
		

if(o>k):
	print("EUSAPIA")
elif(k>o):
	print("BARSANULFO")
else:
	print("EMPATE")