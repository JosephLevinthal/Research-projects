from numpy import*
ve = array(eval(input("Jogadas de Eusapia: ")))
vb = array(eval(input("Jogadas de Barsanulfo: ")))

p = 11 #PEDRA
pa = 22 #PAPEL
t = 33 #TESOURA
#EUSAPIA GANHA:
print(size(ve))

i= 0 
se=0
sb=0

while(i < size(ve)):
	if((ve[i]==11 and vb[i]==33)or(ve[i]==22 and vb[i]==11) or (ve[i]==33 and vb[i]==22)):
		se = se + 1
	if((vb[i]==11 and ve[i]==33)or(vb[i]==22 and ve[i]==11) or (vb[i]==33 and ve[i]==22)):
		sb = sb + 1
	i = i + 1
if(se>sb):
	print('EUSAPIA')
if(se<sb):
	print('BARSANULFO')
if(se==sb):
	print("EMPATE")
	

	
	
	
	
	
	
	