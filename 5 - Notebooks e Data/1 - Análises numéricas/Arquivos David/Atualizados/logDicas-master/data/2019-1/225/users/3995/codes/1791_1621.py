from numpy import*
n=array(eval(input("nomes:")))
v=array(eval(input("quantos?")))

i=0
j=0
t=0

while(i<len(n)):
	if(n[i]=="ARROZ"):
		t=t+(v[i]*1.25)
	elif(n[i]=="FEIJAO"):
		t=t+(v[i]*2.60)
	elif(n[i]=="BIS"):
		t=t+(v[i]*1.80)
	elif(n[i]=="MIOJO"):
		t=t+(v[i]*0.85)
	elif(n[i]=="FANTA"):
		t=t+(v[i]*3.20)
	i=i+1
	j+=t
	
print(round(t,2))