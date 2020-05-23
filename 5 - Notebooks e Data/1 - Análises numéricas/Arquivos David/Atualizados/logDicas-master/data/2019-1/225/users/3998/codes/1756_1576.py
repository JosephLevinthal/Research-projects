from numpy import*
a = array(eval(input("jogadas de Eusapia:" )))
b = array(eval(input("jogadas de Barsanulfo:" )))

e= 0    #variavel contadora de posicao dos vetores
h= 0      #variavel contadora vitoria de eusapia
i= 0       #variavel contadora vitoria de barsanulfo

while(e < size(a)):
	if(a[e]==11)and(b[e]==22):
		i = i+1
	elif(a[e]==22)and(b[e]==33):
		i= i +1
	elif(a[e]==33)and(b[e]==11):
		i=i+1
	elif(a[e]==11)and(b[e]==33):
		h=h+1
	elif(a[e]==22)and(b[e]==11):
		h=h+1	
	elif(a[e]==33)and(b[e]==22):
		h=h+1
	
	e=e+1
print(e)
if(h>i):
	print("EUSAPIA")
elif(h<i):
	print("BARSANULFO")
else:
	print("EMPATE")
