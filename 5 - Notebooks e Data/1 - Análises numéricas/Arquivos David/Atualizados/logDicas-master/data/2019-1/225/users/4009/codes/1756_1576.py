from numpy import*

c=0 #posicaodosvetores
r=0 #vitoriadaeusapia
w=0 #vitoriasdebarsanulfo
e= array(eval(input()))
b= array(eval(input()))

while (c< size(e)):
	if (e[c]!=b[c]):
		if (e[c]==11) and (b[c]==33) or (e[c]==22) and (b[c]==11) or (e[c]==33) and (b[c]==22):
			r=r+1
		elif (b[c]==11) and (e[c]==33) or (b[c]==22) and (e[c]==11) or (b[c]==33) and (e[c]==22):
			w=w+1
	c=c+1
if (r>w):
	print(c)
	print("EUSAPIA")
elif (r==w):
	print(c)
	print("EMPATE")
else:
	print (c)
	print ("BARSANULFO")