from numpy import *

a = array(eval(input("EUSAPIA: ")))
b = array(eval(input("BARSANULFO: ")))

i = 0 #variavel 
eu = 0 #acumula pontos de eusapia
ba = 0 #acumula pontos de barsanulos

while(i < size(a)):
	if(a[i]==11) and (b[i]==22): #barsanulfo
		ba=ba+1
	elif(a[i]==11) and (b[i]==33): #eusapia
		eu=eu+1
	elif(a[i]==22) and (b[i]==11): #eusapia
		eu=eu+1
	elif(a[i]==22) and (b[i]==33): #barsanulfo
		ba=ba+1
	elif(a[i]==33) and (b[i]==22): #eusapia
		eu=eu+1
	elif(a[i]==33) and (b[i]==11): #barsanulfo
		ba=ba+1
	i=i+1
print(i)
if(eu>ba):
	print("EUSAPIA")
elif(ba>eu):
	print("BARSANULFO")
else:
	print("EMPATE")
