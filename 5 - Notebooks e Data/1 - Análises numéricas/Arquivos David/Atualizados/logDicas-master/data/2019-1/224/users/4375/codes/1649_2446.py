#soma dos digitos da SEGUNDA, QUARTA E SEXTA POSIÇÃO
numero=int(input("digite um numero de 6 dig: "))
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
if((d2+d4+d6)%(d1+d3+d5)==0):
	mensagem= "acesso liberado"
	print(mensagem)
else:
	mensagem= "senha invalida"
	print(mensagem)