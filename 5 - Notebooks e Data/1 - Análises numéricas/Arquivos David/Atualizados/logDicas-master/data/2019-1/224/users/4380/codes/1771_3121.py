from numpy import *
e=array(eval(input("jogadas eusapia: ")))
b=array(eval(input("jogadas barsanulfo: ")))
posicao=0
ve=0
vb=0
while (posicao<size(e)):
	if (e[posicao]==33 and b[posicao]==11) or (e[posicao]==22 and b[posicao]==11) or (e[posicao]==33 and b[posicao]==22):
		ve=ve+1
	elif (e[posicao]==11 and b[posicao]==22) or (e[posicao]==11 and b[posicao]==33) or (e[posicao]==22 and b[posicao]==33):
		vb=vb+1
	posicao=posicao+1
if(ve>vb):
	print(size(e))
	print("EUSAPIA")
elif(ve<vb):
	print(size(b))
	print("BARSANULFO")
else:
	print(size(b))
	print("EMPATE")	
