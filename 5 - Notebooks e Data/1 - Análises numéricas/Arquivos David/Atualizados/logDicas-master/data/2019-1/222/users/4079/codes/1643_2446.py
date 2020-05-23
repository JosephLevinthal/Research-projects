senha=float(input("digite a senha:"))
cm= senha//100000
resto_cm=senha % 100000
dm=resto_cm//10000
resto_dm=resto_cm%10000
um=resto_dm//1000
resto_um=resto_dm%1000
cent=resto_um//100
resto_c=resto_um%100
dez=resto_c//10
resto_dez=resto_c%10
resul_1=dm+cent+resto_dez
resul_2=cm+um+dez
if(resul_1%resul_2)==0:
	print("acesso liberado")
else:
	print("senha invalida")