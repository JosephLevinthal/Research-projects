numero=int(input("digite o numero de  6 digito"))
d1=numero//100000
resto=numero%100000
d2=resto//10000
resto=resto%10000
d3=resto//1000
resto=resto%1000
d4=resto//100
resto=resto%100
d5=resto//10
d6=resto%10
if ((d1+d3)%(d2+d4)%(d5+d6) != 0):
	msm="acesso liberado"
else:
	msm="senha invalida"
print(msm)