pira = int(input("qtde. inicial: "))
cresc = int(input("crescimento: "))/100
cont = 0
while(pira>0 and pira<8000):
	pira = pira + (pira*cresc)
	ret=int(input("retirada mensal: "))
	if(pira>=0 and pira<=8000):
		pira = pira - ret
		mensagem = "ZERO"
	else:
		mensagem = "MAXIMO"
	cont = cont + 1
print (mensagem)
print (cont)