from numpy import*
vetor_inicial=array(eval(input("elementos: ")))
aux1=0
aux2=0
aux3=0
qt_positivos=0
while(aux1<size(vetor_inicial)):
	if(vetor_inicial[aux1]>=0):
		qt_positivos = qt_positivos + 1
	aux1=aux1+1	
	v_positivos=zeros(qt_positivos, dtype=int)
while((aux2<size(vetor_inicial))):
	if(vetor_inicial[aux2]>=0):
		v_positivos[aux3]=vetor_inicial[aux2]
		aux3=aux3+1
	aux2=aux2+1
print(v_positivos)	

		