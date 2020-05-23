from numpy import*
saida=int(input("sainda de cidade: "))
destino=int(input("Cidade destino: "))

soma=0
mat=array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])

while (saida!= -1 and destino != -1):
	
	i=(saida%10)-1
	j=(destino%10)-1
	
	soma=soma+mat[i, j]
	saida=destino
	destino=int(input("Cidade de destino: "))
print(soma)