from numpy import*
notas=array(eval(input("notas: ")))
cont=0
aux=0
aux_b=0
v_arange=arange(size(notas))
for i in notas:
	if(i >= 5):
		cont=cont+1
print(cont)	
v_zeros=zeros(cont, dtype=int)
for i in notas:
	if(i>=5):
		v_zeros[aux]=v_zeros[aux]+aux_b
		aux=aux+1
	aux_b=aux_b+1		
print(v_zeros)	