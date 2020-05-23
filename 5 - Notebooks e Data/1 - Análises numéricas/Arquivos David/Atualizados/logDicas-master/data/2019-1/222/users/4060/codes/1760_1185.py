from numpy import*
glicose=array(eval(input("nivel de glicose: ")))
cont_1=0
cont_2=0

while(cont_1<size(glicose)):
	if(glicose[cont_1]>99):
		cont_2=cont_2+1 #acumula a quant. de elementos para os vetores v_zeros e v_crescente
	cont_1=cont_1+1
	v_zeros=zeros(cont_2,dtype=int)
	v_crescente=arange(cont_1)
cont_1=cont_1*0
cont_2=cont_2*0
while(cont_1<size(glicose)):
	if(glicose[cont_1]>99):
		v_zeros[cont_2]=v_crescente[cont_1]#quarda os indices >99 de v_crescente em v_zeros
		cont_2=cont_2+1
		print(cont_1)	
	cont_1=cont_1+1
cont_1=cont_1*0
cont_2=cont_2*0	
while(cont_1<size(glicose)):
	if(glicose[cont_1]>99):
		cont_2=cont_2+1 #acumula a quant. de elementos para o vetor v_ocorrencias
	cont_1=cont_1+1
	v_ocorrencias=cont_2
	
print(v_ocorrencias)

		