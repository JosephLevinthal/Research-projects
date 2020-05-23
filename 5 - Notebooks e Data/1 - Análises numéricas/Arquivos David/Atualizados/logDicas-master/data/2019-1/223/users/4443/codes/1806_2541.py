from numpy import *
p = array(eval(input("Digite os valores para o vetor p: ")))
q = array(eval(input("Digite os valores para o vetor q: ")))
soma = 0
for i in range(size(p)):
	soma = soma + (p[i]-q[i])**2
dist = soma**0.5
print(round(dist, 4))