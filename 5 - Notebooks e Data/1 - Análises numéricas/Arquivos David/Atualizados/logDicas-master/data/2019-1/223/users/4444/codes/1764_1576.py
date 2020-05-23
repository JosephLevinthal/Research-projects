from numpy import *
eusapia=array(eval(input('digite as jogadas de Eurapia:  ')))
barsanulfo=array(eval(input('digite as jogadas de Barsanulfo:  ')))

i=0

b_vence=0
e_vence=0
empate=0

while(i < len(eusapia)):
	
	if (barsanulfo[i]==11 and eusapia[i]==33) or (barsanulfo[i]==22 and eusapia[i]==11) or (barsanulfo[i]==33 and eusapia[i]==22):
		b_vence= b_vence +1
		
	elif (barsanulfo[i]==11 and eusapia[i]==22) or (barsanulfo[i]==22 and eusapia[i]==33) or (barsanulfo[i]==33 and eusapia[i]==11):
		e_vence= e_vence +1
	
	else:
		empate=empate +1
		
	i=i+1
	
print(len(barsanulfo))

if(b_vence > e_vence):
	print("BARSANULFO")
	
elif (e_vence > b_vence):
	print("EUSAPIA")
	
else:
	print('EMPATE')

	
