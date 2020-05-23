from numpy import *
gols_feitos=array(eval(input("gols feitos: ")))
gols_pegos=array(eval(input("gols pegos: ")))
cont=0
v_aux=zeros(3, dtype=int)
for i in gols_feitos:
	if(i>gols_pegos[cont]):#acumula valores para vitorias
		v_aux[0]=v_aux[0]+1
	elif(i == gols_pegos[cont]):#acumula valores para empates
		v_aux[1]=v_aux[1]+1
	elif(i<gols_pegos[cont]):#acumula valores para derrotas
		v_aux[2]=v_aux[2]+1
	cont=cont+1
print(v_aux)
