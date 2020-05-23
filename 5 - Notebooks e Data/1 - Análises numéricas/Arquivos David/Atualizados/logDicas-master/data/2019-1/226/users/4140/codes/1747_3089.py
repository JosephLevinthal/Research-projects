#direita=positivo
#esquerda=negativo
#numero demovimento
#finaliza quando for 0
#imprimir esquerda ou direita
#somatorio
n=int(input())
i=0
s=0
while(n!=0):
	s=s+n
	i=i+1
	n=int(input())
if(s==0):
	print(s)
	print("Inicial")
elif(s>0):
	print(s)
	print("Direita")
else:
	print(s)
	print("Esquerda")