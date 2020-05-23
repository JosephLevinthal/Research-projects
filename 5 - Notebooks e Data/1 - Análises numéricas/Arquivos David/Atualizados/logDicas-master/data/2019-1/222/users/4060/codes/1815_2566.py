from numpy import*
faltas=array(eval(input("informe as faltas: ")))
v_aux=zeros(6, dtype=float)
v_aux2=zeros(6, dtype=float)
v_size=size(faltas)
cont=0
for i in faltas:
	if(i==2):
		v_aux[0]=v_aux[0]+1
	elif(i==3):
		v_aux[1]=v_aux[1]+1
	elif(i==4):
		v_aux[2]=v_aux[2]+1
	elif(i==5):
		v_aux[3]=v_aux[3]+1
	elif(i==6):
		v_aux[4]=v_aux[4]+1
	elif(i==7):
		v_aux[5]=v_aux[5]+1
for i in v_aux:
	v_aux2[cont]=round((i*100)/v_size, 1)
	cont=cont+1
print(v_aux2)
	