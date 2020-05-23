from numpy import*
ve=array(eval(input("digite os vetores de eusapia: ")))
vb=array(eval(input("digite os vetores de barsanulfo: ")))
i=0
some=0
somb=0
valore=0
valorb=0
while(i<size(ve)):
	if(ve[i] == 33 and vb[i] == 22):
		valore= 1
		valorb= 0
	elif(ve[i] == 22 and vb[i] == 11):
		valore= 1
		valorb= 0
	elif(ve[i] == 11 and vb[i] == 33):
		valore= 1
		valorb= 0
	elif(ve[i] == 11 and vb[i] == 11):
		valore= 0
		valorb= 0
	elif(ve[i] == 22 and vb[i] == 22):
		valore= 0
		valorb= 0
	elif(ve[i] == 33 and vb[i] == 33):
		valore= 0
		valorb= 0
	elif(ve[i] == 22 and vb[i] == 33):
		valore= 0
		valorb= 1
	elif(ve[i] == 33 and vb[i] == 11):
		valore= 0
		valorb= 1
	elif(ve[i] == 11 and vb[i] == 22):
		valore= 0
		valorb= 1
	some=some+valore
	somb=somb+valorb
	i=i+1
print(size(ve))
if (some==somb):
	print("EMPATE")
if (some>somb):
	print("EUSAPIA")
if (somb>some):
	print("BARSANULFO")
	
		
	