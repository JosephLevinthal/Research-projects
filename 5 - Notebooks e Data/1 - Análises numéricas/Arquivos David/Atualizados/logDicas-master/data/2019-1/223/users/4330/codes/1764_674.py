from numpy import*
v=array(eval(input("insira o valor do vetor: ")))
#quantidadede elementos do vetor
print(size(v)) # ou len(v)
#primeiro elemento do vetor
print(v[0])
#ultimo elemento do vetor
print(v[-1])
#maior elemento do vetor
print(max(v))
#menor elemento do vetor 
print(min(v))
#soma dos elementos do vetor
print(sum(v))
#media aritmética dos elementos do vetor, com até duas casas decimais de precisão. 
print(round(mean(v),2)) # ou ( sum(v) / size(v))
