from numpy import *
e=array(eval(input("jogadas de eusapia: ")))
b=array(eval(input("jogadas de barsanulfo: ")))
ev=0
bv=0
i=0
print(len(e))
while(i<len(e) and i<len(b)):
	if(b[i]==e[i]):
		i=i+1
	elif(b[i]==11 and e[i]==22):
		ev=ev+1
		i=i+1
	elif(b[i]==11 and e[i]==33):
		bv=bv+1
		i=i+1
	elif(b[i]==22 and e[i]==33):
		ev=ev+1
		i=i+1
	elif(e[i]==11 and b[i]==22):
		bv=bv+1
		i=i+1
	elif(e[i]==11 and b[i]==33):
		ev=ev+1
		i=i+1
	elif(e[i]==22 and b[i]==33):
		bv=bv+1
		i=i+1
if(ev==bv):
	print("EMPATE")
elif(ev>bv):
	print("EUSAPIA")
else:
	print("BARSANULFO")
	
