from numpy import*
#pedra = 11
#papel = 22
#tesoura = 33
E = array(eval(input("jogadas de Eusapia: ")))
B = array(eval(input("jogadas de Barsanulfo: ")))

pv = 0 #posicao dos vetores
VE = 0 #contador de vitorias de Eusápia 
VB = 0 #contador de vitorias de Barsanulfo

while((pv < size(E))):
	
	if((E[pv]==11 and B[pv]==33) or (E[pv]==22 and B[pv]==11) or (E[pv]==33 and B[pv]==22)):
		VE = VE +1
	elif((B[pv]==11 and E[pv]==33) or (B[pv]==22 and E[pv]==11) or (B[pv]==33 and E[pv]==22)):
		VB = VB + 1
	pv = pv + 1

if((VE)>(VB)):
	mensagem = ("EUSAPIA")
elif((VB)>(VE)):
	mensagem = ("BARSANULFO")
else:
	mensagem = ("EMPATE")
print(pv)
print(mensagem)