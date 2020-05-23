from numpy import*
vetor=array(eval(input("FAltas:")))
segunda=0
terca=0
quarta=0
quinta=0
sexta=0
sabado=0
for i in range(size(vetor)):
	if(vetor[i]==2):
		segunda=segunda+1
	elif(vetor[i]==3):
		terca=terca+1
	elif(vetor[i]==4):
		quarta=quarta+1
	elif(vetor[i]==5):
		quinta=quinta+1
	elif(vetor[i]==6):
		sexta=sexta+1
	elif(vetor[i]==7):
		sabado=sabado+1
x=segunda+terca+quarta+quinta+sexta+sabado
y=zeros(6, dtype=float)
for i in range(size(y)):
	y[0]=round(((segunda/x)*100), 1)
	y[1]=round(((terca/x)*100), 1)
	y[2]=round(((quarta/x)*100), 1)
	y[3]=round(((quinta/x)*100), 1)
	y[4]=round(((sexta/x)*100), 1)
	y[5]=round(((sabado/x)*100), 1)
print(y)