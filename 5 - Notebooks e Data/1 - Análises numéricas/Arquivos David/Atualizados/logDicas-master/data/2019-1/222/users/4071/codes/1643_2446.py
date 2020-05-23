senha=int(input('senha: '))
a=senha//100000
restoA=senha%100000
b=restoA//10000
restoB=restoA%10000
c=restoB//1000
restoC=restoB%1000
d=restoC//100
restoD=restoC%100
e=restoD//10
restoE=restoD%10
f=restoE

if(b+d+f)%(a+c+e)==0:
	mensagem="acesso liberado"
else:
	mensagem="senha invalida"
print(mensagem)

