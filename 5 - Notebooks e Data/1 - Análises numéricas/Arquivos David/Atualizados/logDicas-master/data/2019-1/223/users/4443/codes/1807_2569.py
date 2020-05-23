from numpy import *
from math import *
r = array(eval(input("Digite um vetor de n reais: ")))
m = mean(r)
soma = 0
for i in range(size(r)):
	soma = soma + (r[i]-m)**2 #r[i] eh o valor no vetor, que eh subtraido da media e a dif eh elevada ao quadrado
var = soma/(size(r)-1) #a variancai eh dada pela razao entre doma e n-1 elementos do vetor
sd = var**0.5 #SD eh dado pela raiz quadrada da variancia
print(round(sd, 3))	