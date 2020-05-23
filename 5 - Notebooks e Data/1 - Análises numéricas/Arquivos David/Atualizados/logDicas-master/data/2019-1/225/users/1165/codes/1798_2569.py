#Desvio Padrão
from numpy import*
ele=array(eval(input("Valores do vetor: ")))# Valores de x
me=sum(ele)/size(ele)#Média dos valores
d=0 #Acumuladora
for i in range(size(ele)):# Quantidade de repetições
	w=(ele[i]-me)**2
	d=d+w
j=(d/(size(ele)-1))**0.5
print(round(j,3))