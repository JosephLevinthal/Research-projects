from numpy import *
faltas = array(eval(input("Historico de faltas: ")))
vcont = zeros(6)
for i in range(0, size(faltas)):
	dia = faltas[i] - 2
	vcont[dia] = vcont[dia] + 1
for i in range(0, size(vcont)):
	vcont[i] = round(vcont[i]/size(faltas) * 100, 1)
print(vcont)