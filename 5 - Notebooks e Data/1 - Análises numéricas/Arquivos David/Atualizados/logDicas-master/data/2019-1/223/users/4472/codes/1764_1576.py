# Nome: Nathaly Barbosa Leite
# Curso: Estatística
# Matrícula: 21954721

from numpy import *

seqEusapia = array(eval(input("Sequencia de Eusapia: ")))
seqBarsanulfo = array(eval(input("Sequencia de Barsanulfo: ")))

posicao = 0
vitoriaEusapia = 0
vitoriaBarsanulfo = 0


while (posicao < size(seqEusapia)):
	if (seqEusapia[posicao] == 11 and seqBarsanulfo[posicao] == 33) or (seqEusapia[posicao] == 22 and seqBarsanulfo[posicao] == 11) or (seqEusapia[posicao] == 33 and seqBarsanulfo[posicao] == 22):
		vitoriaEusapia += 1	
	elif (seqBarsanulfo[posicao] == 11 and seqEusapia[posicao] == 33) or (seqBarsanulfo[posicao] == 22 and seqEusapia[posicao] == 11) or (seqBarsanulfo[posicao] == 33 and seqEusapia[posicao] == 22):
		vitoriaBarsanulfo += 1	
	posicao = posicao + 1
	
if (vitoriaEusapia > vitoriaBarsanulfo):
	resultado = "EUSAPIA"
	
elif (vitoriaBarsanulfo > vitoriaEusapia):
	resultado = "BARSANULFO"
	
elif (vitoriaEusapia == vitoriaBarsanulfo):
	resultado = "EMPATE"

print (posicao)
print (resultado)