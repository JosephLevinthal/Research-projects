numero=int(input("digite o numero:"))
d1=numero//1000
resto=numero%1000
d2=resto//100
resto=resto%100
d3=resto//10
d4=resto%10
if(d1+d3)%(d2+d4):
	print("senha invalida")
else:
	print("acesso liberado")