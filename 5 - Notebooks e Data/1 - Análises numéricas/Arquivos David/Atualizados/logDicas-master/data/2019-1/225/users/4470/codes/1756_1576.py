from numpy import*
a=array(eval(input("Eusapia: ")))
b=array(eval(input("Barsanulfo: ")))
i=0 # contador 
eu=0 #contador da vitoria do Eusapia
bar=0 #contador da vitoria do Barsanulfo
while(i<size(a)):
	if(a[i]==11)and(b[i]==22): 
		bar=bar+1
	elif(a[i]==11)and(b[i]==33): 
		eu=eu+1
	elif(a[i]==22)and(b[i]==11): 
		eu=eu+1
	elif(a[i]==22)and(b[i]==33): 
		bar=bar+1
	elif(a[i]==33)and(b[i]==11): 
		bar=bar+1
	elif(a[i]==33)and(b[i]==22): 
		eu=eu+1
	i=i+1
print(i)
if(eu>bar):
	print("EUSAPIA")
elif(bar>eu):
	print("BARSANULFO")
else:
	print("EMPATE")