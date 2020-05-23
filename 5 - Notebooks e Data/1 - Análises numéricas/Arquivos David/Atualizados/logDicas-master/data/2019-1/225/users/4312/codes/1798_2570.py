from numpy import*
vetor=array(eval(input("Valores de Xn: ")))# Valor de Xn
me=sum(vetor)/size(vetor)# Média do vetor
mo=1
for i in range(size(vetor)):
	
	mo=mo*abs(vetor[i]-me)# Cálculo interno do módulo

p=mo**(1/size(vetor))# Raiz n
print(round(p,3))